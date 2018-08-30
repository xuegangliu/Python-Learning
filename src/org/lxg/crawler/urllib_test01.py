#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: python
    @Date: 8/30/2018 8:59 PM
    @Author: xuegangliu
    @Description: urllib_test01
"""

from urllib import request

# 网页编码获取
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    print("网页的编码:",chardet.detect(html))
    html = html.decode("utf-8")
    print(html)