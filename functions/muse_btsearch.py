#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-6
# Msg: love or loved?

import requests
from bs4 import BeautifulSoup

engineUrl = 'https://0mag.net/search?q='

def main():
    KeyWord = input('关键词: ')
    target_url = engineUrl + KeyWord
    html_content = requests.get(target_url)
    print(html_content.text)

    # 创建一个BeautifulSoup解析对象
    soup = BeautifulSoup(html_content.text,"html.parser",from_encoding='utf-8')
    # 获取内容
    print('解析中')
    apiGetPage = soup.find_all('td')
    for btlist in apiGetPage:
        if btlist.get_text() == '':
            print('')
        else:
            print(btlist.get_text())

main()