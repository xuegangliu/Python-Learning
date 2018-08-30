#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: python
    @Date: 8/30/2018 9:23 PM
    @Author: xuegangliu
    @Description: urllib_test03
"""

from urllib import request
from  bs4 import BeautifulSoup
import re
import time

def get_url_content(url,code,):
    html = request.urlopen(url).read().decode(code)
    soup = BeautifulSoup(html,'html.parser')
    print(soup.prettify())
    return soup

def get_content_img():
    soup=get_url_content('https://www.zhihu.com/question/22918070','utf-8')
    #用Beautiful Soup结合正则表达式来提取包含所有图片链接（img标签中，class=**，以.jpg结尾的链接）的语句
    links = soup.find_all('img', "origin_image zh-lightbox-thumb",src=re.compile(r'.jpg$'))
    print(links)
    return links

def save_img_to_file(path):
    links=get_content_img()
    for link in links:
        print(link.attrs['src'])
        #保存链接并命名，time.time()返回当前时间戳防止命名冲突
        request.urlretrieve(link.attrs['src'],path+'\%s.jpg' % time.time())  #使用request.urlretrieve直接将所有远程链接数据下载到本地

if __name__ == "__main__":
    save_img_to_file(path = r'D:\sample\img')
