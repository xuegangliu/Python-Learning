#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    @Project: python
    @Date: 10/14/2018 10:58 AM
    @Author: xuegangliu
    @Description: fileTest
"""
import os

def test():
    print(os.getcwd())
    print(os.listdir())
    # print(os.path.join(os.getcwd(),os.listdir()[1]))

def writeFileList():
    fid = open('fileList.txt', 'w')
    # rootdir = os.getcwd()
    rootdir = 'D:\\test'
    print('rootdir = ' + rootdir)
    pathname = []
    for (dirpath, dirnames, filenames) in os.walk(rootdir):
        for filename in filenames:
            pathname += [os.path.join(dirpath, filename)]
    for tt in pathname:
        fid.write(str(tt))
        fid.write("\n")
    fid.close()

if __name__ == '__main__':
    # test()
    writeFileList()