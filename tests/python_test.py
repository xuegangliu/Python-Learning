#!/usr/bin/python
# coding=utf-8
# author: xuegangliu

import pdb

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


if __name__ == '__main__':
    # print(make_bread())

    a = [1,2,4,5,6]
    b = {'a':1,'b':3}
    test_arg(*a,**b)