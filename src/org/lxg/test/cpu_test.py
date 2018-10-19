#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: python
    @Date: 10/19/2018 1:27 PM
    @Author: xuegangliu
    @Description: cpu_test
"""

import psutil
import os
import subprocess # 创建子进程

def cpu_test():
    #获取当前运行的pid
    p1=psutil.Process(os.getpid())
    print("当前pid",p1)
    while True:
        a = psutil.virtual_memory().percent  #内存占用率
        b = psutil.cpu_percent(interval=1.0) #cpu占用率
        print('内存占用率:'+str(a),'cpu占用率:'+str(b))

def test1():
    config_path = os.getenv("config_path")
    print(config_path)
    home = os.path.expanduser("~")
    print(home)

def subprocess_test():
    # 创建子进程
    subprocess.call(['java','-h'])

if __name__ == '__main__':
    cpu_test()
    # test1()
    # subprocess_test