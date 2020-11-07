#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-4
# Msg: love or loved?

import json
import requests

# API
ipPositionAPIURL = 'https://api.bilibili.com/x/web-interface/zone'

## IP定位
def main():
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