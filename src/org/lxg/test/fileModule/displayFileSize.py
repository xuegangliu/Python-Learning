#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: python
    @Date: 10/18/2018 11:13 AM
    @Author: xuegangliu
    @Description: displayFileSize
"""
import os
import time

def TimeStampToTime(timestamp):
    """
    把时间戳转化为本地时间并格式化
    :param timestamp:
    :return:
    """
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def displayDirectory(directory):
    """
    显示目录下所有文件列表及大小
    :param directory:文件目录
    """
    print("目录:"+directory)
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath,filename)
            if os.path.isfile(filepath):
                print('文件名:'+filename,'文件大小:'+str(os.path.getsize(filepath))+'KB',
                      '访问时间:'+TimeStampToTime(os.path.getatime(filepath)),
                      '创建时间:'+TimeStampToTime(os.path.getctime(filepath)),
                      '修改时间:'+TimeStampToTime(os.path.getmtime(filepath)))

if __name__ == '__main__':
    displayDirectory("D:\\test")