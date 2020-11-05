print('Program Start')
import requests
import json
import webbrowser
import os
import time
import _thread

# SYS INFO

Version = '0.01'
VersionNickName = 'loved'
Coder = 'D0OR.TEA'
SupportUrl = 'https://muse.obent.cn/'

# MOEGIRL
def moeGirl():
    print('-'*20)
    print("  く__,.ヘヽ.        /  ,ー､ 〉")
    print("           ＼ ', !-─‐-i  /  /´")
    print("           ／｀ｰ'       L/／｀ヽ､")
    print("         /   ／,   /|   ,   ,       ',")
    print("       ｲ   / /-‐/  ｉ  L_ ﾊ ヽ!   i")
    print("        ﾚ ﾍ 7ｲ｀ﾄ   ﾚ'ｧ-ﾄ､!ハ|   |")
    print("          !,/7 '0'     ´0iソ|    |")
    print("          |.从'    _     ,,,, / |./    |")
    print("          ﾚ'| i＞.､,,__  _,.イ /   .i   |")
    print("            ﾚ'| | / k_７_/ﾚ'ヽ,  ﾊ.  |")
    print("              | |/i 〈|/   i  ,.ﾍ |  i  |")
    print("             .|/ /  ｉ：    ﾍ!    ＼  |")
    print("              kヽ>､ﾊ    _,.ﾍ､    /､!")
    print("              !'〈//｀Ｔ´', ＼ ｀'7'ｰr'")
    print("              ﾚ'ヽL__|___i,___,ンﾚ|ノ")
    print("                  ﾄ-,/  |___./")
    print("                  'ｰ'    !_,.:")
    print('-'*20)
    # time.sleep(1)


# MuseCodeLogo
def MuseCodeLogo():
    print("                ..        ..        ..      ..         ....            ...:.::          ")
    print("               QBB       QBB       QBB     BQv       :BBQBBBB        BBBBBBBBB          ")
    print("              1QBr     :XBB       UBB     BB1       BB2   BBB       QQB                 ")
    print("             rQBB:    qBBB       rBB     BBP       BBY   .KU       SBQ                  ")
    print("            .BBBB.  SEBBB.      .BB.    QBB       .BB5I           7BBBgBBg              ")
    print("            BBBBD  ZBBBBi       BBi    KBB         ..BBBP        :BB..irr:              ")
    print("           QB: QBBBD BBs       BBv    sBB             .BB.       BB:                    ")
    print("          BB5 dBBBQ PBb       MBM    vBB.      rBB    BBJ       BB:                     ")
    print("         BBB  BBB  QBB        :BB7:qBB         BBM.:iBB5       BBB..ii7.                ")
    print("        :Bg  :Qg  .Bg          5gQBB           rMRBBB2        vBZZQBQBQ:        V:",Version,'By:',Coder,"      ")


# API配置
checkUploadUrl = 'http://106.55.26.167/musebot/nowver.php' 
aiTalkAPI = 'https://api.qingyunke.com/api.php?key=free&appid=0&msg='
ipPositionAPIURL = 'https://api.bilibili.com/x/web-interface/zone'
dailyHimgAPIURL = 'https://api.lolicon.app/setu/?r18=1'
baiduSearchAPI = 'https://www.baidu.com/s?ie=UTF-8&wd='

# 分割线
def dividingLine():
    print('-' * 10)

# 命令菜单
def Menu():
    print('-'*20)
    print('* 按照提示输入对应单词以进入功能')
    print('~'*10,'% 基本功能 %','~'*10)
    print('[aitalk] *AI女友        [ip] *IP定位')
    print('[ping] *PING            [cmd] *CMD DOS系统')
    print('[baidu] *百度搜索            [news] *新闻先知')
    print('~'*10,'% 系统设置 %','~'*10)
    print('[upgrade] *更新Bot      [reboot] *重启Bot')
    print('[shutdown] *关闭Bot     [about-muse] *关于Muse')

# 检查更新
def checkUpload():
    print('正在检查更新......')
    uploadURL = checkUploadUrl
    nowver = Version
    newver = requests.get(uploadURL)
    json_str = json.loads(newver.text)
    # 判断是否更新
    if Version < json_str['v']:
        print('* 有新版本!')
        print('* 当前版本:',Version,'最新版本:',json_str['v'])
        print('* 下载地址:',json_str['url'])
        print('更新日志')
        print(json_str['up-note'])
        # webbrowser.open(json_str['url']) 自动打开网址已禁用
    else:
        print('无需更新')

# 功能
## AI交流
def aiTalk():
    print('* 对话模式,输入 [quit] 退出对话模式')
    print('MuseBot: Hi~')
    while True:
        KeyWord = input('我: ')
        if KeyWord == 'quit':
            print('-'*20)
            print('MuseBot: 你真的要走嘛o(╥﹏╥)o')
            print('* 输入 [y/n] 选择退出(y:yes ; n:no)')
            quit_confirm = input('[y/n] : ')
            if quit_confirm == 'y':
                print('MuseBot: 拜拜qwq,挤得下次来找我哟(＾Ｕ＾)ノ~ＹＯ')
                break
            elif quit_confirm == 'n':
                print('-'*20)
                print('MuseBot: 我就知道你舍不得我qwq,那就再聊会吧')
            else:
                print('哈?听不懂~那就当不退出咯')
                print('-'*20)
        else:
            aiAPI = aiTalkAPI+KeyWord
            json_content = requests.get(aiAPI)
            json_str = json.loads(json_content.text)
            print('MuseBot:',json_str['content'])

print('aiTalk Standby.')

## IP定位
def ipPosition():
    print('正在获取当前IP')
    ipPositionAPI = ipPositionAPIURL
    json_content = requests.get(ipPositionAPI)
    json_str = json.loads(json_content.text)
    if json_str['code'] == 0:
        print('IP:',json_str['data']['addr'],'位置:',json_str['data']['country'],json_str['data']['province'],json_str['data']['city'])
        print('经纬度:','经:',json_str['data']['longitude'],'纬:',json_str['data']['latitude'])
    else:
        print('获取失败,请重试')

print('ipPosition Standby.')

## 每日色图
# * (由于接口被反爬处理,该功能被禁用)
# def dailyHimg():
#     print('正在获取每日色图')
#     dailyHimgAPI = dailyHimgAPIURL
#     json_content = requests.get(dailyHimgAPI)
#     json_str = json.loads(json_content.text)
#     if json_str['code'] == 0:
#         webbrowser.open(json_str['data']['0']['url'])
#     elif json_str['code'] == -1:
#         print('API内部错误')
#     elif json_str == 403:
#         print('被拒绝调用,请重试')
#     elif json_str == 429:
#         print('调用次数达每日上限')

print('dailyHimg ERROR.')

## PING命令
def pingCommand():
    targetUrl = input('输入目标地址或网址: ')
    os.system('ping '+targetUrl)
    

print('pingCommand Standby')

# 基础欢迎
def models():
    print('-'*20)
    print('MuseBot')
    print('-'*20)
    print('v',Version,'by:',Coder)
    print('SupportUrl:',SupportUrl)
# time.sleep(1)

# CMD
def doscmd():
    print('* 已进入CMD模式')
    print('* 输入exit退出')
    os.system('cmd')

# Reboot
def reboot():   # 此功能需要多线程实现
    def reboot_open_new_bot():
        program_path = os.getcwd()
        os.system('python ' + program_path + '\muse.py')
    def reboot_close_bot():
        os._exit()
    try:
        _thread.start_new_thread(reboot_open_new_bot)
        _thread.start_new_thread(reboot_close_bot)
    except:
        print('多线程重启失败\n1秒后被迫使用单线程重启')
        time.sleep(1)
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
            moeGirl()
            time.sleep(1)
            os._exit()
        elif chose == 'n':
            print('取消关闭')
            break
        else:
            print('???')

# baiduSearch
def baiduSearch():
    KeyWord = input('关键词: ')
    url = baiduSearchAPI+KeyWord
    webbrowser.open(url)

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
    nowver = Version
    newver = requests.get(uploadURL)
    json_str = json.loads(newver.text)
    print('最新版本:',json_str['v'])
    print('当前版本代号:',VersionNickName)
    print('版本作者:',Coder)
    print('支持连接:',SupportUrl)
    print('#'*10,'@ 我的故事 @','#'*10)
    print('> 我见到她的第一面,就喜欢上了她...')
    print('> 可她说“我们只能做朋友”....')
    print('Muse,慕涩的恋情。\n代指我在喜欢她的时候，仰慕她，但又羞涩止步于喜欢。。。\n也许是我喜欢的方式不对,又或许是我不够优秀...\n或许都是...')

# Main
os.system('title MuseBot V:'+Version)
MuseCodeLogo() # MUSE LOGO
print('\n')
moeGirl() # 开机颜文字
os.system('clear') # 前面模组加载完后,清理加载提示
checkUpload() # 检查更新
models() # 基础欢迎
Menu() #欢迎菜单

# 让👴来判断你的选择吧
while True:
    # 用户输入
    print('-' * 20)
    user_chose = input('My: ')
    print('-' * 20)
    if user_chose == 'aitalk':
        os.system('clear')
        aiTalk()
    elif user_chose == 'ip':
        ipPosition()
    elif user_chose == '':
        pass
    elif user_chose == 'ping':
        pingCommand()
    elif user_chose == 'cmd':
        doscmd()
    elif user_chose == 'setu':
        print('由于接口被反爬处理,该功能被禁用') # 色图功能禁用
    elif user_chose == 'baidu':
        baiduSearch()
    elif user_chose == 'cls':
        os.system('clear')
    elif user_chose == 'upgrade':
        checkUpload()
    elif user_chose == 'reboot':
        reboot()
    elif user_chose == 'shutdown':
        shutdownbot()
    elif user_chose == 'help':
        Menu()
    elif user_chose == 'about-muse':
        aboutmuse()
    elif user_chose == 'well':
        print('well?well what?')
    elif user_chose == '智者不入爱河':
        print('愚者为情所困,作者就是愚者,但可惜的是作者都没有机会变成"愚者"')
    else:
        print('输错了单词?还是想跟我聊聊?')
        print('输入 [help] 来获取命令菜单')
        print('或输 [aitalk] 来获取与我聊天')
