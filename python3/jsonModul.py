#!/usr/bin/python
# -*- coding:utf-8 -*-
import json

def functionJson():
  print('----functionJson')
  data1 = {
    'no':1,
    'name':'lxg',
    'age':25
  }
  json_str=json.dumps(data1)
  print('Python原数据:',repr(data1))
  print('JSON对象:',json_str)
  data2 = json.loads(json_str)
  print("data2['name']:",data2['name'])
  print("data2['age']:",data2['age'])
