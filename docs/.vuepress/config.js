module.exports = {
  title: '自冻 FreezeYou',
  description: '自冻 FreezeYou',
  locales: {
    '/zh-CN/': {
      lang: 'zh-CN',
      title: '自冻',
      description: '自冻'
    },
    '/en-US/': {
      lang: 'en-US',
      title: 'FreezeYou',
      description: 'FreezeYou!'
    }
  },
  head: [
    ['link', { rel: 'icon', href: '/assets/img/logo.svg' }],
    ['link', { rel: 'manifest', href: '/assets/manifest.json' }],
    ['meta', { name: 'theme-color', content: '#2B60FF' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }],
    ['link', { rel: 'apple-touch-icon', href: `/assets/icons/apple-touch-icon-152x152.png` }],
    ['link', { rel: 'mask-icon', href: '/assets/icons/safari-pinned-tab.svg', color: '#2B60FF' }],
    ['meta', { name: 'msapplication-TileImage', content: '/assets/icons/msapplication-icon-144x144.png' }],
    ['meta', { name: 'msapplication-TileColor', content: '#000000' }]
  ],
  plugins: [
    ['@vuepress/plugin-pwa'],
    [
      '@vuepress/plugin-pwa-popup',
      {
        locales: {
          '/': {
            message: 'New content is available.',
            buttonText: 'Refresh',
          },
          '/zh-CN/': {
            message: "发现有内容更新",
            buttonText: "刷新",
          },
          '/en-US/': {
            message: "New content is available.",
            buttonText: "Refresh",
          },
        },
      },
    ],
    ['@vuepress/plugin-back-to-top'],
    [
      '@vuepress/plugin-search',
      {
        locales: {
          '/en-US/': {
            placeholder: 'Search',
          },
          '/zh-CN/': {
            placeholder: '搜索',
          },
        },
      },
    ],
  ],
  themeConfig: {
    locales: {
      '/zh-CN/': {
        editLinkText: '编辑此页',
        lastUpdatedText: '最后更新于',
        selectLanguageText: '语言',
        selectLanguageName: '简体中文(中国大陆)',
        navbar: [
          { text: '首页', link: '/zh-CN/' },
          { text: '开始', link: '/zh-CN/guide/' },
          { text: '下载', link: '/zh-CN/download/' },
          { text: 'FAQ', link: '/zh-CN/faq/' },
          { text: 'API', link: '/zh-CN/api/' },
          { text: '日志', link: '/zh-CN/changelog/' },
          {
            text: '更多',
            children: [
              {
                text: '关于自冻',
                children: [
                  { text: '联系我们', link: '/zh-CN/about/contactUs.md' },
                  { text: '特别感谢', link: '/zh-CN/thanks/' },
                  { text: '状态监控', link: 'https://status.zidon.net' },
                  { text: 'GitHub', link: 'https://github.com/FreezeYou/' },
                ],
              },
              {
                text: '友情链接',
                children: [
                  { text: '秋之盒', link: 'https://atmb.top/?from=freezeyou' },
                  { text: 'Zidon.NET', link: 'https://www.zidon.net' },
                  { text: 'FreezeYou.NET', link: 'https://www.freezeyou.net' },
                  { text: '自冻.COM', link: 'https://www.xn--f8qp88i.com/' },
                  { text: '旧版站点', link: 'https://freezeyou.playhi.net' },
                ],
              },
            ],
          },
        ],
        sidebar: {
          '/zh-CN/guide/': getGuideSidebar('开始', '更新日志', 'FAQ', 'API'),
          '/zh-CN/download/': getGuideSidebar('开始', '更新日志', 'FAQ', 'API'),
          '/zh-CN/changelog/': getGuideSidebar('开始', '更新日志', 'FAQ', 'API'),
          '/zh-CN/api/': getGuideSidebar('开始', '更新日志', 'FAQ', 'API'),
          '/zh-CN/faq/': getGuideSidebar('开始', '更新日志', 'FAQ', 'API')
        },
        searchPlaceholder: '搜索',
        backToHome: '返回首页',
        notFound: [
          `这里怎么空荡荡的？`,
          `咦，怎么到这里来了？`,
          `四零四了！`,
          `咦，这个页面跑丢了！`
        ],
      },
      '/en-US/': {
        editLinkText: 'Edit this page',
        lastUpdatedText: 'Last Updated',
        selectLanguageText: 'Language',
        selectLanguageName: 'English(US)',
        navbar: [
          { text: 'Home', link: '/en-US/' },
          { text: 'Guide', link: '/en-US/guide/' },
          { text: 'Download', link: '/en-US/download/' },
          { text: 'FAQ', link: '/en-US/faq/' },
          { text: 'API', link: '/en-US/api/' },
          { text: 'Changelog', link: '/en-US/changelog/' },
          {
            text: 'More',
            children: [
              {
                text: 'About',
                children: [
                  { text: 'Contact Us', link: '/en-US/about/contactUs.md' },
                  { text: 'Special Thanks', link: '/en-US/thanks/' },
                  { text: 'Server Status', link: 'https://status.zidon.net' },
                  { text: 'GitHub Organization', link: 'https://github.com/FreezeYou/' },
                ],
              },
              {
                text: 'Link',
                children: [
                  { text: 'AutumnBox', link: 'https://atmb.top/?from=freezeyou' },
                  { text: 'Zidon.NET', link: 'https://www.zidon.net' },
                  { text: 'FreezeYou.NET', link: 'https://www.freezeyou.net' },
                  { text: 'xn--f8qp88i.COM', link: 'https://www.xn--f8qp88i.com/' },
                  { text: 'Old Site', link: 'https://freezeyou.playhi.net' },
                ],
              },
            ],
          },
        ],
        sidebar: {
          '/en-US/guide/': getGuideSidebar('Guide', 'Changelog', 'FAQ', 'API'),
          '/en-US/download/': getGuideSidebar('Guide', 'Changelog', 'FAQ', 'API'),
          '/en-US/changelog/': getGuideSidebar('Guide', 'Changelog', 'FAQ', 'API'),
          '/en-US/api/': getGuideSidebar('Guide', 'Changelog', 'FAQ', 'API'),
          '/en-US/faq/': getGuideSidebar('Guide', 'Changelog', 'FAQ', 'API')
        },
        searchPlaceholder: 'Search',
        backToHome: 'Take me home.',
        notFound: [
          `There's nothing here.`,
          `How did we get here?`,
          `That's a Four-Oh-Four.`,
          `Looks like we've got some broken links.`
        ],
      },
    },
    navbar: false,
    sidebar: 'auto',
    sidebarDepth: 1,
    displayAllHeaders: true,
    activeHeaderLinks: true,
    logo: '/assets/img/logo.svg',
    repo: 'https://github.com/FreezeYou/Website',
    repoLabel: 'GitHub',
    docsRepo: 'https://github.com/FreezeYou/Website',
    docsDir: 'docs',
    docsBranch: 'master',
    editLink: true,
    editLinkPattern: ':repo/edit/:branch/:path',
    contributors: false,
    lastUpdated: true,
    smoothScroll: true,
    nextLinks: true,
    prevLinks: true,
    search: true,
    searchMaxSuggestions: 10
  }
}

function getGuideSidebar(guide, changelog, faq, api) {
  return [
    {
      isGroup: true,
      text: guide,
      collapsable: true,
      children: [
        '../guide/',
        '../guide/warning.md',
        '../download/',
        '../guide/how-to-use.md',
        '../guide/enable-mroot.md',
        '../guide/schedules.md'
      ]
    },
    {
      isGroup: true,
      text: faq,
      collapsable: true,
      children: [
        '../faq/',
        '../faq/mroot.md',
        '../faq/daily.md',
        '../faq/schedules.md'
      ]
    },
    {
      isGroup: true,
      text: api,
      collapsable: true,
      children: [
        '../api/',
        '../api/uri.md',
        '../api/provider.md',
        '../api/start-activity.md'
      ]
    },
    {
      isGroup: true,
      text: changelog,
      collapsable: true,
      children: [
        '../changelog/'
      ]
    }
  ]
}
