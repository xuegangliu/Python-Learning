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
import argparse
import operator

def TimeStampToTime(timestamp):
    """
    把时间戳转化为本地时间并格式化
    :param timestamp:
    :return:
    """
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def displayDirectory(directory,sizeSwitch):
    """
    显示目录下所有文件列表及大小
    :param directory:文件目录
    """
    print("目录:"+directory)
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath,filename)
            if os.path.isfile(filepath):
                if operator.eq(sizeSwitch,"KB"):
                    print('文件名:'+filename,'文件大小:'+str(os.path.getsize(filepath))+'KB',
                          '访问时间:'+TimeStampToTime(os.path.getatime(filepath)),
                          '创建时间:'+TimeStampToTime(os.path.getctime(filepath)),
                          '修改时间:'+TimeStampToTime(os.path.getmtime(filepath)))
                if operator.eq(sizeSwitch,'MB'):
                    print('文件名:'+filename,'文件大小:'+str(round(os.path.getsize(filepath)/float(1024*1024),2))+'MB',
                          '访问时间:'+TimeStampToTime(os.path.getatime(filepath)),
                          '创建时间:'+TimeStampToTime(os.path.getctime(filepath)),
                          '修改时间:'+TimeStampToTime(os.path.getmtime(filepath)))
def get_parser():
    parser = argparse.ArgumentParser(description='显示目录下所有文件列表')
    parser.add_argument('size', metavar='size', type=str, nargs=1, help='按KB|MB显示文件大小')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = vars(parser.parse_args())
    sizeSwitch = str(args['size'][0]).split('=')[1]
    displayDirectory("D:\\test",sizeSwitch)