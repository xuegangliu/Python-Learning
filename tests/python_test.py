#!/usr/bin/python
# coding=utf-8
# author: xuegangliu

import pdb
import configparser
from functools import reduce
import os

# pdb断点使用
def make_bread():
    # c: 继续执行
    # w: 显示当前正在执行的代码行的上下文信息
    # a: 打印当前函数的参数列表
    # s: 执行当前代码行，并停在第一个能停的地方（相当于单步进入）
    # n: 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）
    pdb.set_trace() # 设置断点
    return "I don't have time"

# *var与**var1用法
def test_arg(*var,**var1):
    print('###############################')
    print(type(var))
    for i in var:
        print('*var')
        print(i)
    print('##############  **var1  ################')
    for key,value in var1.items():
        print('**var')
        print('%s,%s'%(key,value))

def test_config():
    cf = configparser.ConfigParser()
    # cf.read('../config/test.conf')
    cf.read('../config/test.ini')

    #return all section
    secs = cf.sections()
    print('sections:', secs, type(secs))
    opts = cf.options("db")
    print('options:', opts, type(opts))
    kvs = cf.items("db")
    print('db:', kvs)

    #read by type
    db_host = cf.get("db", "db_host")
    db_port = cf.getint("db", "db_port")
    db_user = cf.get("db", "db_user")
    db_pass = cf.get("db", "db_pass")

    #read int
    threads = cf.getint("concurrent", "thread")
    processors = cf.getint("concurrent", "processor")
    print("db_host:", db_host)
    print("db_port:", db_port)
    print("db_user:", db_user)
    print("db_pass:", db_pass)
    print("thread:", threads)
    print("processor:", processors)

    # write to file
    cf.remove_section('concurrent')
    with open("../config/test2.ini","w+") as f:
        cf.write(f)

# map filter reduce 测试
def test_map_filter_reduce():
    funcs = [multiply, add]
    for i in range(5):
        value = map(lambda x: x(i), funcs)
        print('map():',list(value))
    print('filter():',list(filter(lambda x: x < 0, range(-5, 5))))
    print('reduce():',reduce( (lambda x, y: x * y), [1, 2, 3, 4] ))
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

def main():
    # print(make_bread())

    # a = [1,2,4,5,6]
    # b = {'a':1,'b':3}
    # test_arg(*a,**b)

    # test_config()

    test_map_filter_reduce()

if __name__ == '__main__':
    main()