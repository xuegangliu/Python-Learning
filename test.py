#!/usr/bin/python
# coding=utf-8
# author: xuegangliu

'''
python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
'''

import tests.module_test as module_test

if __name__ == '__main__':
    module_test.test_module()
    print('bulid success!!')