#!/usr/bin/python3
import os
import re
import time
import json

translations = {}
cwd = os.getcwd()
regex = re.compile(r'{{@.+?}}')
select_language_page_locales_template = '''\
* <a href="javascript:forwardTo('{{@translation_country_key}}');">{{@selectLanguageName}}</a>
'''
config_js_locales_template = '''
    '/{{@translation_country_key}}/': {
      lang: '{{@translation_country_key}}',
      title: '{{@heroText}}',
      description: '{{@heroText}}'
    },
'''
config_js_pwa_popup_template = '''
          '/{{@translation_country_key}}/': {
            message: "{{@newContentIsAvailable}}",
            buttonText: "{{@refresh}}",
          },
'''
config_js_search_template = '''
          '/{{@translation_country_key}}/': {
            placeholder: '{{@search}}',
          },
'''
config_js_theme_config_template = '''
      '/{{@translation_country_key}}/': {
        editLinkText: '{{@editThisPage}}',
        lastUpdatedText: '{{@lastUpdated}}',
        selectLanguageText: '{{@language}}',
        selectLanguageName: '{{@selectLanguageName}}',
        navbar: [
          { text: '{{@homePage}}', link: '/{{@translation_country_key}}/' },
          { text: '{{@guidePage}}', link: '/{{@translation_country_key}}/guide/' },
          { text: '{{@download}}', link: '/{{@translation_country_key}}/download/' },
          { text: '{{@faqPage}}', link: '/{{@translation_country_key}}/faq/' },
          { text: '{{@API}}', link: '/{{@translation_country_key}}/api/' },
          { text: '{{@changelogPage}}', link: '/{{@translation_country_key}}/changelog/' },
          {
            text: '{{@more}}',
            children: [
              {
                text: '{{@aboutPage}}',
                children: [
                  { text: '{{@contactUs}}', link: '/{{@translation_country_key}}/about/contactUs.md' },
                  { text: '{{@specialThanks}}', link: '/{{@translation_country_key}}/thanks/' },
                  { text: '{{@serverStatus}}', link: 'https://status.zidon.net' },
                  { text: '{{@gitHubOrganization}}', link: 'https://github.com/FreezeYou/' },
                ],
              },
              {
                text: '{{@linkPage}}',
                children: [
                  { text: '{{@autumnBox}}', link: 'https://atmb.top/?from=freezeyou' },
                  { text: 'Zidon.NET', link: 'https://www.zidon.net' },
                  { text: 'FreezeYou.NET', link: 'https://www.freezeyou.net' },
                  { text: '{{@xn--f8qp88i.COM}}', link: 'https://www.xn--f8qp88i.com/' },
                  { text: '{{@oldSite}}', link: 'https://freezeyou.playhi.net' },
                ],
              },
            ],
          },
        ],
        sidebar: {
          '/{{@translation_country_key}}/guide/': getGuideSidebar('{{@guidePage}}', '{{@changelog}}', '{{@faqPage}}', '{{@API}}'),
          '/{{@translation_country_key}}/download/': getGuideSidebar('{{@guidePage}}', '{{@changelog}}', '{{@faqPage}}', '{{@API}}'),
          '/{{@translation_country_key}}/changelog/': getGuideSidebar('{{@guidePage}}', '{{@changelog}}', '{{@faqPage}}', '{{@API}}'),
          '/{{@translation_country_key}}/api/': getGuideSidebar('{{@guidePage}}', '{{@changelog}}', '{{@faqPage}}', '{{@API}}'),
          '/{{@translation_country_key}}/faq/': getGuideSidebar('{{@guidePage}}', '{{@changelog}}', '{{@faqPage}}', '{{@API}}')
        },
        searchPlaceholder: '{{@search}}',
        backToHome: '{{@backToHome}}',
        notFound: [
          `{{@notFound_1}}`,
          `{{@notFound_2}}`,
          `{{@notFound_3}}`,
          `{{@notFound_4}}`
        ],
      },
'''


def print_log(log, category="INFO", style="0;30"):
    print("\033[{0}m{1} [{2}] {3}\033[0m".format(
        style, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), category, log))


def load_translation_file():
    path = cwd + "/translations"
    file_list = os.listdir(path)
    for tmp in file_list:
        tmp_path = os.path.join(path, tmp)
        if os.path.isfile(tmp_path) and tmp_path[tmp_path.rfind('.') + 1:].lower() == 'json':
            with open(tmp_path, 'r') as f:
                translations[tmp_path[tmp_path.rfind('/') + 1:tmp_path.rfind('.')]] = json.load(f)
                print_log("Translation file loaded: " + tmp, "INFO", "0;36")


def pre_generate_documents_for_vuepress(path):
    file_list = os.listdir(path)
    for tmp in file_list:
        tmp_path = os.path.join(path, tmp)
        if os.path.isdir(tmp_path):
            pre_generate_documents_for_vuepress(tmp_path)
        elif tmp_path[tmp_path.rfind('.') + 1:].lower() == 'md':
            with open(tmp_path, 'r') as f:
                template_content = f.read()
                for translation_country_key in translations.keys():
                    if translation_country_key == 'default':
                        continue
                    output_file_path = \
                        cwd + "/docs/" + translation_country_key + tmp_path[len(cwd) + 9:]
                    os.makedirs(output_file_path[:output_file_path.rfind("/")], 0o777, True)
                    generated_content = template_content
                    placeholders = regex.findall(generated_content)
                    for placeholder in placeholders:
                        key = placeholder[3:-2]
                        generated_content = generated_content.replace(
                            placeholder,
                            translations[translation_country_key].get(
                                key, translations['default'][key]
                            )
                        )
                    existed_content = None
                    if os.path.exists(output_file_path):
                        read_mode_output_file = open(output_file_path, "r")
                        existed_content = read_mode_output_file.read()
                        read_mode_output_file.close()
                    if generated_content == existed_content:
                        print_log(
                            "Document is up to date: " + output_file_path[len(cwd) + 1:],
                            "INFO", "0;36"
                        )
                    else:
                        with open(
                                output_file_path,
                                "w+"
                        ) as output:
                            output.write(generated_content)
                        print_log(
                            "Document generated: " + output_file_path[len(cwd) + 1:],
                            "INFO", "0;36"
                        )


def pre_generate_config_js_and_select_lang_page_for_vuepress(
        config_js_template_path, lang_page_template_path, lang_js_template_path
):
    config_js_locales_generated = ""
    config_js_pwa_popup_generated = ""
    config_js_search_generated = ""
    config_js_theme_config_generated = ""
    select_language_page_locales_generated = ""
    for translation_country_key in sorted(translations.keys()):
        if translation_country_key == 'default':
            continue
        if translations[translation_country_key].get(
                "selectLanguageName",
                translations['default']["selectLanguageName"]
        ) == "In progress":
            continue

        generated_locales_content = config_js_locales_template.replace(
            '{{@translation_country_key}}', translation_country_key)
        placeholders = regex.findall(generated_locales_content)
        for placeholder in placeholders:
            key = placeholder[3:-2]
            generated_locales_content = generated_locales_content.replace(
                placeholder,
                translations[translation_country_key].get(
                    key, translations['default'][key]
                )
            )
        config_js_locales_generated += generated_locales_content

        generated_pwa_popup_content = config_js_pwa_popup_template.replace(
            '{{@translation_country_key}}', translation_country_key)
        placeholders = regex.findall(generated_pwa_popup_content)
        for placeholder in placeholders:
            key = placeholder[3:-2]
            generated_pwa_popup_content = generated_pwa_popup_content.replace(
                placeholder,
                translations[translation_country_key].get(
                    key, translations['default'][key]
                )
            )
        config_js_pwa_popup_generated += generated_pwa_popup_content

        generated_search_content = config_js_search_template.replace(
            '{{@translation_country_key}}', translation_country_key)
        placeholders = regex.findall(generated_search_content)
        for placeholder in placeholders:
            key = placeholder[3:-2]
            generated_search_content = generated_search_content.replace(
                placeholder,
                translations[translation_country_key].get(
                    key, translations['default'][key]
                )
            )
        config_js_search_generated += generated_search_content

        generated_theme_config_content = config_js_theme_config_template.replace(
            '{{@translation_country_key}}', translation_country_key)
        placeholders = regex.findall(generated_theme_config_content)
        for placeholder in placeholders:
            key = placeholder[3:-2]
            generated_theme_config_content = generated_theme_config_content.replace(
                placeholder,
                translations[translation_country_key].get(
                    key, translations['default'][key]
                )
            )
        config_js_theme_config_generated += generated_theme_config_content

        generated_lang_page_content = select_language_page_locales_template.replace(
            '{{@translation_country_key}}', translation_country_key)
        placeholders = regex.findall(generated_lang_page_content)
        for placeholder in placeholders:
            key = placeholder[3:-2]
            generated_lang_page_content = generated_lang_page_content.replace(
                placeholder,
                translations[translation_country_key].get(
                    key, translations['default'][key]
                )
            )
        select_language_page_locales_generated += generated_lang_page_content

    with open(config_js_template_path, 'r') as input_file:
        source = input_file.read()
        with open(cwd + '/docs/.vuepress/config.js', 'w') as output_file:
            output_file.write(
                source.replace(
                    "/*{{@locales_content}}*/", config_js_locales_generated, 1
                ).replace(
                    "/*{{@pwa_popup_content}}*/", config_js_pwa_popup_generated, 1
                ).replace(
                    "/*{{@pwa_search_content}}*/", config_js_search_generated, 1
                ).replace(
                    "/*{{@pwa_theme_config_content}}*/",
                    config_js_theme_config_generated, 1
                )
            )
        print_log("File config.js generated.", "INFO", "0;36")

    with open(lang_page_template_path, 'r') as input_file:
        source = input_file.read()
        with open(cwd + '/docs/README.md', 'w') as output_file:
            output_file.write(
                source.replace(
                    "<!--{{@locales_generated_content}}-->",
                    select_language_page_locales_generated, 1
                )
            )
        print_log(
            "File SelectLanguagePage.markdown to README.md generated.",
            "INFO", "0;36"
        )

    with open(lang_js_template_path, 'r') as input_file:
        source = input_file.read()
        available_langs = []
        for translation_country_key in sorted(translations.keys()):
            if translation_country_key == 'default':
                continue
            if translations[translation_country_key].get(
                    "selectLanguageName",
                    translations['default']["selectLanguageName"]
            ) != "In progress":
                available_langs.append(translation_country_key)

        with open(cwd + '/docs/.vuepress/public/assets/js/lang.min.js', 'w') as output_file:
            output_file.write(
                source.replace(
                    "/*{{@locales_availableLangs}}*/",
                    str(available_langs), 1
                )
            )
        print_log(
            "File lang.js and lang.min.js generated.",
            "INFO", "0;36"
        )


print_log("Current working directory: " + cwd, "INFO", "0;35")
print_log("Loading translation files...", "INFO", "0;34")
load_translation_file()
print_log("Generating translated documents for vuepress...", "INFO", "0;34")
pre_generate_documents_for_vuepress(cwd + "/template")
pre_generate_config_js_and_select_lang_page_for_vuepress(
    cwd + "/template/config.js",
    cwd + "/template/SelectLanguagePage.markdown",
    cwd + "/template/lang.min.js"
)
print_log("Done.", "INFO", "0;32")
print_log(
    "It's the time for using vuepress to generate the final documents!",
    "INFO", "0;32"
)
