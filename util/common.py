#!/usr/bin/python
# coding: utf-8
# author: xuegangliu
# date: 20180824

"""
各种常用类库
"""
import logging
import logging.handlers
from ConfigParser import ConfigParser
from collections import namedtuple
import os
import shutil
import glob
import sys
import time
import datetime


class ColorPrint:
    """
    进行高亮输出运行信息
    """

    def __init__(self):
        pass

    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARING = '\033[95m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @staticmethod
    def log_normal(info):
        print(ColorPrint.OKBLUE + info + ColorPrint.ENDC)

    @staticmethod
    def log_high(info):
        print(ColorPrint.OKGREEN + info + ColorPrint.ENDC)

    @staticmethod
    def log_warn(info):
        print(ColorPrint.WARING + info + ColorPrint.ENDC)

    @staticmethod
    def log_fail(info):
        print(ColorPrint.FAIL + info + ColorPrint.ENDC)