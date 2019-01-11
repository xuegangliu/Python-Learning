"""
    @Project: python
    @Date: 2018/9/2 0:26
    @Author: xuegangliu
    @Description: yield_test
"""
from random import randint
import asyncio,random

'''
Python中的协程三个阶段： 
1. 最初的生成器变形yield/send 
2. 引入@asyncio.coroutine和yield from 
3. 在最近的Python3.5版本中引入async/await关键字
'''

def mygen(alist):
    while len(alist) > 0:
        c = randint(0, len(alist)-1)
        yield alist.pop(c)
def mygen_test():
    a = ["aa","bb","cc"]
    c=mygen(a)
    print(c)

def gen():
    value=0
    while True:
        receive=yield value
        if receive=='e':
            break
        value = 'got: %s' % receive
def gen_test():
    g=gen()
    print(g.send(None))
    print(g.send('hello'))
    print(g.send(123456))
    print(g.send('e'))

def g1():
    yield  range(5)
def g2():
    yield  from range(5)
def g1_g2_test():
    it1 = g1()
    it2 = g2()
    for x in it1:
        print(x)

    for x in it2:
        print(x)
def f_wrapper(fun_iterable):
    print('start')
    for item  in fun_iterable:
        yield item
    print('end')
def f_wrapper_test():
    wrap = f_wrapper(fab(5))
    for i in wrap:
        print(i,end=' ')
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

def f_wrapper2(fun_iterable):
    print('start')
    yield from fun_iterable  #注意此处必须是一个可生成对象
    print('end')
def f_wrapper2_test():
    wrap = f_wrapper2(fab(5))
    for i in wrap:
        print(i,end=' ')

@asyncio.coroutine
def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.2)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('Smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1

@asyncio.coroutine
def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 0.4)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1
def stupid_fib_test():
    loop = asyncio.get_event_loop()
    tasks = [
        smart_fib(10),
        stupid_fib(10),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()

async def mygen_await(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist)-1)
        print(alist.pop(c))
        await asyncio.sleep(1)
def mygen_await_test():
    strlist = ["ss","dd","gg"]
    intlist=[1,2,5,6]
    c1=mygen(strlist)
    c2=mygen(intlist)
    print(c1)

if __name__ == '__main__':
    # mygen_test()
    # gen_test()

    # g1_g2_test()
    # f_wrapper_test()
    # f_wrapper2_test()

    # stupid_fib_test()

    mygen_await_test()