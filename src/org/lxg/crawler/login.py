#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: python
    @Date: 8/30/2018 9:53 PM
    @Author: xuegangliu
    @Description: login
"""

import urllib.request
import http.cookiejar
import urllib.parse

def getOpener(header):
    '''构造文件头'''
    # 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
    cookieJar = http.cookiejar.CookieJar()
    cp = urllib.request.HTTPCookieProcessor(cookieJar)
    opener = urllib.request.build_opener(cp)
    headers = []
    for key,value in header.items():
        elem = (key,value)
        headers.append(elem)
    opener.addheaders = headers
    return opener

def html_login(url,headers,postDict):
    '''构造登陆信息进行登陆'''
    req=urllib.request.Request(url,headers=headers)
    res=urllib.request.urlopen(req)
    data = res.read()
    opener = getOpener(headers)
    #给post数据编码
    postData=urllib.parse.urlencode(postDict).encode()
    #构造请求
    res=opener.open(url,postData)
    data = res.read()
    print(data.decode())

if __name__ == "__main__":
    url = "test"
    # 根据网站报头信息设置headers
    headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en;q=0.6',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'host',
        'DNT':'1'
    }
    #分析构造post数据
    postDict={
        'aa':1,
        'bb':2,
        'cc':3
    }
    html_login(url,headers,postDict)