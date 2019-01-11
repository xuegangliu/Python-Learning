#!/usr/bin/python
# coding=utf-8
# author: xuegangliu


def foo(*args, **kwargs):
    '''*args, **kwargs 参数使用'''
    print('args =', args)
    print('kwargs = ', kwargs)
    print('-----------------------')


if __name__ == '__main__':
    foo(1, 2, 3, 4)
    foo(a=1, b=2, c=3)
    foo(1,2,3,4, a=1, b=2, c=3)
    foo('a', 1, None, a=1, b='2', c=3)