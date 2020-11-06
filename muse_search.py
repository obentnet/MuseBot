#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-4
# Msg: love or loved?

import requests
import webbrowser


# API
baiduSearchAPI = 'https://www.baidu.com/s?ie=UTF-8&wd='
googleSearchAPI = 'https://www.google.com/search?q='

# baiduSearch
def baiduSearch():
    KeyWord = input('关键词: ')
    url = baiduSearchAPI+KeyWord
    webbrowser.open(url)

# GoogleSearch
def googleSearch():
    KeyWord = input('关键词: ')
    url = googleSearchAPI+KeyWord
    webbrowser.open(url)