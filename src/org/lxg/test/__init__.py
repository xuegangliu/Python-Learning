#!/usr/bin/python
# coding=utf-8
# author: xuegangliu

import os,sys,time
sys.path.append(os.path.abspath("./../../../"))
import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)

async def hello1():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

def  consumer_work(len):
    # 读取send传进的数据，并模拟进行处理数据
    print("writer:")
    w=''
    while True:
        w = yield w    # w接收send传进的数据,同时也是返回的数据
        print('[CONSUMER] Consuming %s...>> ', w)
        w*=len #将返回的数据乘以100
        time.sleep(0.1)
def consumer(coro):
    yield from coro#将数据传递到协程(生成器)对象中


def produce(c):
    c.send(None)# "prime" the coroutine
    for i in range(5):
        print('[Produce] Producing %s----', i)
        w=c.send(i)#发送完成后进入协程中执行
        print('[Produce] receive %s----', w)
    c.close()



if __name__ == '__main__':

    # yield 与 yield from
    c1=consumer_work(100)
    produce(consumer(c1))

    # hello()
    # hello1()

    # print(os.path.abspath("./../../../"))
    # print(r'D:\WorkSpaces\Self\python\src')