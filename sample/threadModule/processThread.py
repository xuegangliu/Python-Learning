#!/usr/bin/env org.lxg.python3
# -*- coding: UTF-8 -*-

import multiprocessing
import time
from multiprocessing import Pool
import os, time, random

'''1、类 Process'''
def worker(interval, name):
    print(name + '【start】')
    time.sleep(interval)
    print(name + '【end】')
def workerTest():
    p1 = multiprocessing.Process(target=worker, args=(2, '两点水1'))
    p2 = multiprocessing.Process(target=worker, args=(3, '两点水2'))
    p3 = multiprocessing.Process(target=worker, args=(4, '两点水3'))

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print("END!!!!!!!!!!!!!!!!!")

'''2、把进程创建成类'''
class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("当前时间: {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1
def clockProcessTest():
    p = ClockProcess(3)
    p.start()

'''3、daemon 属性'''
def workerTest1(interval):
    print('工作开始时间：{0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.ctime()))

def long_time_task(name):
    print('进程的名称：{0} ；进程的PID: {1} '.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('进程 {0} 运行了 {1} 秒'.format(name, (end - start)))
def long_time_taskTest():
    print('主进程的 PID：{0}'.format(os.getpid()))
    p = Pool(4)
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))
    p.close()
    # 等待所有子进程结束后在关闭主进程
    p.join()
    print('【End】')

if __name__ == "__main__":
    # workerTest()
    # clockProcessTest()
    # workerTest1(5)
    long_time_taskTest()