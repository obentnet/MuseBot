#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-4
# Msg: love or loved?
import requests
import pygame

api = 'http://music.163.com/song/media/outer/url?id='

def main():
    print('选择一个解析模式：')
    print('[1] 音乐ID')
    print('-'*20)
    music_chose = input('My: ')
    if music_chose == '1':
        print('-'*20)
        song_name = input('歌曲ID: ')
        print('解析中...')
        post_url = api+song_name+'.mp3'
        # print(post_url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        # 获取重写后的的地址
        url_re = requests.get(post_url,headers=headers)
        print('-'*20)
        print('音乐直连地址:')
        print(url_re.url)
    else:
        print('输了些啥...自动退出咯...')


    # 先下再播

    # print('PYGAME PLAYER')
    # pygame.init()
    # pygame.mixer.music.load("Nova7.mp3") # 载入音乐
    # pygame.mixer.music.set_volume(0.2) # 设置音量
    # pygame.mixer.music.play() # 播放音乐