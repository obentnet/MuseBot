#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-4
# Msg: love or loved?

import requests
import json

#Hitokoto
HitokotoApi = 'https://v1.hitokoto.cn'

def main():
    print("""
            您想听什么类型的?
            [a] 动画  [d] 文学
            [b] 漫画  [c] 游戏
            [e] 原创  [f] 来自网络
            [g] 其他  [h] 影视
            [i] 诗词  [j] 网易云
            [k] 哲学  [l] 抖机灵
            * 其他按 [a] 动漫类型输出
        """)
    hitokoto_c = input('我想听: ')
    # 空格报错,使用简单判断来设定默认值
    if hitokoto_c == '':    
        hitokoto_c = 'a'
    else:
        pass

    hitokoto_num = int(input('听几句? :'))
    startnum = 0
    while startnum < hitokoto_num:
        url = HitokotoApi+'?c='+hitokoto_c
        url_content = requests.get(url)
        json_str = json.loads(url_content.text)
        print(json_str['hitokoto']+'出自: 《'+json_str['from']+'》\n')
        startnum += 1