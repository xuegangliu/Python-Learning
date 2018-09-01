#!/usr/bin/python
#coding=utf-8
#import json

import sys,os

sys.path.append(os.path.abspath("./../../../"))

from org.lxg.python3 import jsonModul

def functionHello(a):
  '''这里是Hello函数的doc'''
  print('----functionHello')
  print(a)

'''数字猜谜游戏'''
def functionIf():
  print('----functionIf')
  number = 7
  guess = -1
  print("数字猜谜游戏!")
  while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
      print("恭喜，你猜对了！")
    elif guess < number:
      print("猜的数字小了...")
    elif guess > number:
      print("猜的数字大了...")

def functionType():
  print('----functionType')
  t1,t2,t3=1,100.01,'ok'
  t4=[1,2,3,4,5,'ddd',10.01]
  t5=(1,2,3,4)
  t6={'A','B'}
  t7={'name':'lxg'}
  print(t1,type(t1))
  print(t2,type(t2),end=' ')
  print(t3,type(t3),sep='| ')
  print(t4,type(t4))
  print(t5,type(t5))
  print(t6,type(t6))
  print(t7,type(t7))

# 这是入口
if __name__ == '__main__':
  print(sys.argv)
  try:
    print('-----------------------------------')
    functionHello('您好!')
    print(functionHello.__doc__)
    #functionIf()
    functionType()
    jsonModul.functionJson()
    print(sys.argv)
    print('-----------------------------------')
  except ValueError:
    print('this is Exception!!!')
