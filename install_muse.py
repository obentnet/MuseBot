#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-4
# Msg: love or loved?

import os
import json

# 读取配置文件
config_path = os.getcwd()+'\\config.json'
content = open(config_path)
config_json_str = json.load(content)

mirrorUrl = config_json_str['pipmirrorsurl']

print('正在准备安装所需环境...')

print(
    """
        |``Python3.x``|
        |``os``|
        |``re``|
        |``sys``|
        |``time``|
        |``json``|
        |``pygame``|
        |``_thread``|
        |``requests``|
        |``webbrowser``|
        |``BeautifulSoup``|
    """
)

print('install [ requests ]')
os.system('pip install -i '+mirrorUrl+' requests')

print('install [ beautifulsoup ]')
os.system('pip install -i '+mirrorUrl+' beautifulsoup')

print('install [ pygame ]')
os.system('pip install -i '+mirrorUrl+' pygame')

print('运行完毕,请开启[muse.py] ，如若报错,请重新运行此程序或前往[https://github.com/obentnet/MuseBot/issues]反馈问题')