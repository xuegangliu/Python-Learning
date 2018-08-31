#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: python
    @Date: 8/31/2018 3:56 PM
    @Author: xuegangliu
    @Description: __init__
"""

import os

if __name__ == '__main__':
    db_file = os.path.join(os.path.dirname(__file__), 'test.db')
    print('__file__:',__file__)
    print('os.path:',os.path)
    print(os.path.dirname(__file__))
    print(db_file)

    # print("aa".join("xxx",'5'))
    # print(db_file)
    # if os.path.isfile(db_file):
    #     os.remove(db_file)
