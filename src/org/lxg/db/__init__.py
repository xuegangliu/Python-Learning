#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: python
    @Date: 8/31/2018 3:56 PM
    @Author: xuegangliu
    @Description: __init__
"""

import os
import sys

if __name__ == '__main__':
    db_file = os.path.join(os.path.dirname(__file__), 'test.db')
    print('os.path.dirname(__file__):',os.path.dirname(__file__))
    print("os.path.join(os.path.dirname(__file__), 'test.db')",db_file)

    # 当前模块的文件名
    print('__file__:',__file__)
    # 当前路径的绝对路径
    print('os.path.abspath("."):',os.path.abspath("."))
    # 获取命令行参数
    print('sys.argv:',sys.argv)
    # 获取当前Python命令的可执行文件路径
    print('sys.executable',sys.executable)

    # print("aa".join("xxx",'5'))
    # print(db_file)
    # if os.path.isfile(db_file):
    #     os.remove(db_file)
