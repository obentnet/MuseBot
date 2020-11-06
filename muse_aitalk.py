#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-4
# Msg: love or loved?

import json
import requests

# API
aiTalkAPI = 'https://api.qingyunke.com/api.php?key=free&appid=0&msg='

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
