#!/usr/bin/python
# coding=utf-8
# author: xuegangliu

import sys,os

'''
python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
'''
sys.path.append(os.path.abspath('src/org'))

import org.lxg.test.module_test

if __name__ == '__main__':
    org.lxg.test.module_test.test_module()
    print('bulid success!!')