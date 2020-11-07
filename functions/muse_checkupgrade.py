#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-4
# Msg: love or loved?

import os
import json
import requests
# SYS INFO

Version = '0.10'
VersionNickName = 'loved'
Coder = 'D0OR.TEA'
SupportUrl = 'https://github.com/obentnet/MuseBot'

# API
checkUploadUrl = 'http://106.55.26.167/musebot/nowver.php' 

# 检查更新
def main():
    print('正在检查更新......')
    uploadURL = checkUploadUrl
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
