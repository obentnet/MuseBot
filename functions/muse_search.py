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
bingSearchAPI = 'https://cn.bing.com/search?q='
dogeSeachAPI = 'https://www.dogedoge.com/results?q='
magiSeachAPI = 'https://magi.com/search?q='
lookaoSeachAPI = 'https://lookao.com/search?q='
duckduckgoSearchAPI = 'https://duckduckgo.com/?q='
mijiSearchAPI = 'https://mijisou.com/?q='
sogouSearchAPI = 'https://www.sogou.com/web?query='
safeSearchAPI = 'https://www.so.com/s?q='


# baiduSearch
def baiduSearch():
    KeyWord = input('关键词: ')
    url = baiduSearchAPI + KeyWord
    webbrowser.open(url)

# GoogleSearch
def googleSearch():
    KeyWord = input('关键词: ')
    url = googleSearchAPI + KeyWord
    webbrowser.open(url)

# BingSearch
def bingSearch():
    KeyWord = input('关键词: ')
    url = bingSearchAPI + KeyWord
    webbrowser.open(url)

# DogeSeach
def dogeSeach():
    KeyWord = input('关键词: ')
    url = dogeSeachAPI + KeyWord
    webbrowser.open(url)

# MagiSeach
def magiSeach():
    KeyWord = input('关键词: ')
    url = magiSeachAPI + KeyWord
    webbrowser.open(url)

# Lookao
def lookaoSeach():
    KeyWord = input('关键词: ')
    url = lookaoSeachAPI + KeyWord
    webbrowser.open(url)

# DuckDuckGo
def duckduckgoSearch():
    KeyWord = input('关键词: ')
    url = duckduckgoSearchAPI + KeyWord
    webbrowser.open(url)

# 秘迹搜索
def mijiSearch():
    KeyWord = input('关键词: ')
    url = mijiSearchAPI + KeyWord
    webbrowser.open(url)

# 搜狗搜索
def sogouSearch():
    KeyWord = input('关键词: ')
    url = sogouSearchAPI + KeyWord
    webbrowser.open(url)

# 360搜索
def safeSearch():
    KeyWord = input('关键词: ')
    url = safeSearchAPI + KeyWord
    webbrowser.open(url)