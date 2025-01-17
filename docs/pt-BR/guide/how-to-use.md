# Quick Start
`自冻FreezeYou`的功能非常之多，这里对一部分内容做些简短的介绍，方便快速入门。

## Grant Permissions
`自冻FreezeYou`中的一些功能，需要一些特殊权限，就比如`冻结与解冻`就需要特殊授权才能正常使用（若不使用相关功能，可不授予权限），目前，如要使用`冻结与解冻`功能，需要保证以下至少一个权限已经或能够授予`自冻FreezeYou`，并在`更多设置` - `冻结与解冻` - `选择冻结解冻模式`中选中相应的模式：
* Device Policy Manager (DPM) (Usually be called NoRoot) → How to [grant permission](./enable-mroot.html)
* Root
* System App

## Freeze and Unfreeze <Badge text="Be extra cautious" type="warning"/>
启动`自冻FreezeYou`，待主界面列表载入完成后，点击相应的应用，选择`冻结/解冻/启动`即可进行冻结与解冻操作。

## View by Category <Badge text="1.13+" type="tip"/>
默认情况下，启动`自冻FreezeYou`后首页会直接展示全部的应用，这时，如果想要寻找一些应用，有时会比较麻烦，那么，可以点击右上角的`⋮`或是右下角的`+`或是设备上的`≡`，唤出菜单，点击`查看模式(分类查看)`，即可根据需要分类进行查看。

## Quick Search <Badge text="2.13+" type="tip"/>
启动`自冻FreezeYou`后，在显示的主界面中，点击顶端附近的`搜索`，即可进行快速搜索。  
如，输入`A`即会立即筛选并列出该分类中所有名称中包含`A`或`a`的应用（不区分大小写）。

## Scheduled Task <Badge text="6.0+" type="tip"/>
计划任务的功能比较多，也较为复杂，这里我们单独进行 → [Introdução](./schedules.html)。

## Change Interface Style <Badge text="4.0+" type="tip"/>
启动`自冻FreezeYou`，点击右上角的`⋮`或是右下角的`+`或是设备上的`≡`，唤出菜单，选择`更多设置`，选择`常规`，点击`界面风格`即可修改。

## Backup and Restore <Badge text="8.8+" type="tip"/>
启动`自冻FreezeYou`，点击右上角的`⋮`或是右下角的`+`或是设备上的`≡`，唤出菜单，选择`更多设置`，再选择`备份与还原`，点击`导出`即可将当前的设置、计划任务等数据导出，点击`导入`，会读入下方输入框中的数据，整理后供选择需要导入的数据项。

## Notification Tiles
通过通知栏瓷块，可点击瓷块快速执行操作。下拉通知栏，点击`编辑`，将相应的瓷块设为显示，然后完成编辑后即可使用（需要 Android 系统支持）。  
__Available notification tiles:__  
* One Key Freeze
* One Key Unfreeze
* One Key Screen Lock

## One Key Freeze
`一键冻结`会对每一个存在于`一键冻结列表`中的应用执行`冻结`操作，使用前，需要先将需要被执行的应用添加到`一键冻结列表`中（点击主界面列表中的相应应用，选择`加入/移出`，即可添加）。  
**Usage:**  
* 启动`自冻FreezeYou`，点击右上角的`⋮`或是右下角的`+`或是设备上的`≡`，唤出菜单，选择`立即执行`，最后选择`一键冻结`即可。
* 启动`自冻FreezeYou`，点击右上角的`⋮`或是右下角的`+`或是设备上的`≡`，唤出菜单，选择`快捷方式`，再选择`一键冻结`，即可在桌面上通过快捷方式进行`一键冻结`。
* 唤出桌面的`添加小部件`或是`添加微件`或是`添加小工具`菜单，选择`自冻FreezeYou`，再选择`一键冻结`，即可在桌面上通过快捷方式进行`一键冻结`。

## One Key Unfreeze
`一键解冻`会对每一个存在于`一键解冻列表`中的应用执行`解冻`操作，使用前，需要先将需要被执行的应用添加到`一键解冻列表`中（点击主界面列表中的相应应用，选择`加入/移出`，即可添加）。  
__Usage:__  
* 启动`自冻FreezeYou`，点击右上角的`⋮`或是右下角的`+`或是设备上的`≡`，唤出菜单，选择`立即执行`，最后选择`一键解冻`即可。
* 启动`自冻FreezeYou`，点击右上角的`⋮`或是右下角的`+`或是设备上的`≡`，唤出菜单，选择`快捷方式`，再选择`一键解冻`，即可在桌面上通过快捷方式进行`一键解冻`。
* 唤出桌面的`添加小部件`或是`添加微件`或是`添加小工具`菜单，选择`自冻FreezeYou`，再选择`一键解冻`，即可在桌面上通过快捷方式进行`一键解冻`。

## Leave Freeze
_It is recommended to use `Scheduled Task` instead_  
启动`自冻FreezeYou`，点击右上角的`⋮`或是右下角的`+`或是设备上的`≡`，唤出菜单，选择`更多设置`，选择`自动化`，再勾选`离开冻结`即可，离开在`离开冻结列表`（点击主界面列表中的相应应用，选择`加入/移出`，即可添加）里的相应应用时对应的应用会被冻结。

## Auto One Key Freeze After Screen Locked
_It is recommended to use `Scheduled Task` instead_  
启动`自冻FreezeYou`，点击右上角的`⋮`或是右下角的`+`或是设备上的`≡`，唤出菜单，选择`更多设置`，选择`自动化`，再勾选`锁屏后一键冻结`即可，锁屏后会执行`一键冻结`。

## Preciso de ajuda
* [FAQ](../faq/)
* [Join QQ Group(704086494)](https://jq.qq.com/?_wv=1027&k=5RJffet)

