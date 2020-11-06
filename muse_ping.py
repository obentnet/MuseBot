#!/usr/bin/python
# -*- coding: UTF-8 -*-

# MuseBot
# By:D0OR.TEA
# CreatTime: 2020-11-4
# Msg: love or loved?

import os

## PING命令
def main():
    targetUrl = input('输入目标地址或网址: ')
    os.system('ping '+targetUrl)
print('pingCommand Standby')