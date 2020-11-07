#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-4
# Msg: love or loved?
print('System is running...')
import os,re,sys,time,json,_thread,requests,webbrowser
from bs4 import BeautifulSoup
# model
from functions import muse_ipc,muse_cmd,muse_menu,muse_ping,muse_music,muse_search,muse_aitalk,muse_moegirl,muse_hitokoto,muse_ipposition,muse_checkupgrade
os.system("title System Staring...")

# SYS INFO
Version = '0.10'
Coder = 'D0OR.TEA'
VersionNickName = 'loved'
SupportUrl = 'https://github.com/obentnet/MuseBot'

# API
checkUploadUrl = 'http://106.55.26.167/musebot/nowver.php' 

# MuseCodeLogo
def MuseCodeLogo():
    print("""
                  QBB       QBB       QBB     BQv       :BBQBBBB        BBBBBBBBB         
                 1QBr     :XBB       UBB     BB1       BB2   BBB       QQB                
                rQBB:    qBBB       rBB     BBP       BBY   .KU       SBQ                 
               .BBBB.  SEBBB.      .BB.    QBB       .BB5I           7BBBgBBg             
               BBBBD  ZBBBBi       BBi    KBB         ..BBBP        :BB..irr:             
              QB: QBBBD BBs       BBv    sBB             .BB.       BB:                   
             BB5 dBBBQ PBb       MBM    vBB.      rBB    BBJ       BB:                    
            BBB  BBB  QBB        :BB7:qBB         BBM.:iBB5       BBB..ii7.""")
    print("                                                                              V:",Version,'By:',Coder,"")
        
# 基础欢迎
def models():
    print('-'*20)
    print('MuseBot')
    print('-'*20)
    print('v',Version,'by:',Coder)
    print('SupportUrl:',SupportUrl)

# Reboot
def reboot():   # 此功能需要多线程实现
    def reboot_open_new_bot():
        program_path = os.getcwd()
        os.system('python ' + program_path + '\\muse.py')
    def reboot_close_bot():
        os._exit()
    reboot_open_new_bot()
    reboot_close_bot()

# ShutdownBot
def shutdownbot(): 
    while True:
        print('-'*20)
        print('你确定要关闭MuseBot么?')
        chose = input('[y/n]: ')
        if chose == 'y':
            os.system('clear')
            print('正在关闭MuseBot')
            muse_moegirl.main() # 显示Moegirl
            time.sleep(1)
            sys.exit(0)
        elif chose == 'n':
            print('取消关闭')
            break
        else:
            print('???')

# clearCache 清除[__pycache__]缓存
def clearCache():
    fileurl = os.getcwd()
    cacheurl = fileurl+'\\__pycache__'
    print('即将清理:'+cacheurl)
    print('清理完成后,程序将自动重启,是否确定?')
    confirm = input('[y/n]: ')
    if confirm == 'y':
        print('清理中...')
        os.remove(cacheurl)
    elif confirm == 'n':
        print('取消清理')
    else:
        print('你输了些啥')

def comand_cls():
    os.system('clear')

# about-muse
def aboutmuse():
    os.system('clear')
    MuseCodeLogo()
    print('\n')
    print('~'*10,'% MUSE BOT %','~'*10)
    print('   “智者不入爱河,愚者为情所困.”')
    print('#'*10,'@ 关于系统 @','#'*10)
    print('='*34)
    print('# MuseBot')
    print('当前版本:',Version)

    uploadURL = checkUploadUrl
    newver = requests.get(uploadURL)
    json_str = json.loads(newver.text)

    print('最新版本:',json_str['v'])
    print('当前版本代号:',VersionNickName)
    print('版本作者:',Coder)
    print('支持连接:',SupportUrl)
    print('鸣谢: Ghosin,奇趣宝罗')
    print("""声明: 此程序为开源程序,可任意修改分发使用,但请不要用作商业用途! 后果自负.
    另如果有更改后分发需求,请务必留下一个著作权.[MuseBot By D0OR.TEA]""")
    print('#'*10,'@ 我的故事 @','#'*10)
    print("""
> 我见到她的第一面,就喜欢上了她...
> 可她说“我们只能做朋友”....
Muse,慕涩的恋情。
代指我在喜欢她的时候，仰慕她，但又羞涩止步于喜欢。。。
也许是我喜欢的方式不对,又或许是我不够优秀...又或许都是...
    """)

# 读取配置文件
config_path = os.getcwd()+'\\config.json'
content = open(config_path)
config_json_str = json.load(content)

# 主程序运行
os.system('title MuseBot V:'+Version)
MuseCodeLogo() # MUSE LOGO
print('\n')
muse_moegirl.main() # 开机颜文字
os.system('clear') # 前面模组加载完后,清理加载提示

# 判断并执行是否检查更新
if config_json_str['startupgrade'] == True:
    muse_checkupgrade.main() # 检查更新
elif config_json_str['startupgrade'] == False:
    pass
else:
    print('配置文件出错,请检查config.json')
# 检查更新结束

models() # 基础欢迎

# 判断并执行是否输出菜单
if config_json_str['startmenu'] == True:
    muse_menu.main()
elif config_json_str['startmenu'] == False:
    pass
else:
    print('配置文件出错,请检查config.json')

# 让👴来判断你的选择吧 2.0
while True:
    comands = {
        # 功能命令
        'aitalk' : muse_aitalk.aiTalk,
        'ip' : muse_ipposition.main,
        'ping' : muse_ping.main,
        'cmd' : muse_cmd.main,
        'icp' : muse_ipc.main,
        'netmusic' : muse_music.main,
        'hitokoto' : muse_hitokoto.main,
        ## 搜索引擎
        'baidu' : muse_search.baiduSearch,
        'google' : muse_search.googleSearch,
        'bing' : muse_search.bingSearch,
        'dogeso' : muse_search.dogeSeach,
        'magi' : muse_search.magiSeach,
        'lookao' : muse_search.lookaoSeach,
        'duckso' : muse_search.duckduckgoSearch,
        'miji' : muse_search.mijiSearch,
        'sogou' : muse_search.sogouSearch,
        'safeso' : muse_search.safeSearch,
        # Bot指令
        'help' : muse_menu.main, # 菜单的两种指令
        'menu' : muse_menu.main, # 菜单的两种指令
        'upgrade' : muse_checkupgrade.main,
        'reboot' : reboot,
        'clearcache' : clearCache,
        'shutdown' : shutdownbot,
        'about-muse' : aboutmuse,
        # 基础指令
        'cls' : comand_cls,
        'clear' : comand_cls
        # Trigger Word [关键词触发]
    }
    try:
        print('-' * 20)
        need_run_comand = input('My: ')
        print('-' * 20)
        run_command = comands[need_run_comand]
        run_command()
    except:
        print("""
        输错了单词?还是想跟我聊聊?
        输入 [menu] 来获取命令菜单
        或输 [aitalk] 来获取与我聊天
        """)