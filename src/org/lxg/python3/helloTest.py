#!/usr/bin/python
# coding=utf-8
# author: xuegangliu
# description: 测试

import sys

class User(object):
    def __new__(cls, *args, **kwargs):
        # 打印 __new__方法中的相关信息
        print('调用了 def __new__ 方法')
        print(args)
        # 最后返回父类的方法
        return super(User, cls).__new__(cls)
    def __init__(self):
        print('调用了 def __init__ 方法')

    # def __init__(self, name, age):
    #     print('调用了 def __init__ 方法')
    #     self.name = name
    #     self.age = age

    def __del__(self):
        print('调用了 def __del__ 方法')

    def __getattr__(self, name):
        print('调用了 __getattr__ 方法')
        return super(User, self).__getattr__(name)

    def __setattr__(self, name, value):
        print('调用了 __setattr__ 方法')
        return super(User, self).__setattr__(name, value)

    def __delattr__(self, name):
        print('调用了 __delattr__ 方法')
        return super(User, self).__delattr__(name)

    def __getattribute__(self, name):
        print('调用了 __getattribute__ 方法')
        return super(User, self).__getattribute__(name)

if __name__ == '__main__':
    # print(sys.path)
    # print(sys.version)
    # print(dir(A()))

    # 有参数
    # usr = User('两点水', 23)

    user = User()
    # 设置属性值，会调用 __setattr__
    user.attr1 = True
    # 属性存在,只有__getattribute__调用
    user.attr1
    try:
        # 属性不存在, 先调用__getattribute__, 后调用__getattr__
        user.attr2
    except AttributeError:
        pass
    # __delattr__调用
    del user.attr1