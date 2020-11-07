import os
import re
import time
import json
import _thread
import requests
import webbrowser

from bs4 import BeautifulSoup
icpQueryUrl = 'http://icp.chinaz.com/home/info?host='

# ICP查询
def main():
    target_url = input('输入查询目标网址: ')
    url = icpQueryUrl+target_url
    html_doc = requests.get(url)
    #创建一个BeautifulSoup解析对象
    soup = BeautifulSoup(html_doc.content,"html.parser",from_encoding="utf-8")
    # 获取所有的内容
    print ("正在获取并解析内容...")
    print('-'*20)
    print('ICP备案主体信息:')
    content_ele = soup.find_all('td')
    for content in content_ele:
        if content.get_text() == '':
            pass
        else:
            print(content.get_text())