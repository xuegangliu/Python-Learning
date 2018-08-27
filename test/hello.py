#!/usr/bin/python
# coding=utf-8
# author: xuegangliu

import sys
'''
python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
'''
sys.path.append(r'D:\WorkSpaces\Self\python\test\xmlModule')

import json
import xml.dom.minidom
import xml.sax

import domModule
import saxModule

# hello function
def hello():
	arrayss=[1,2,3,4,5]
	total=1+ \
		  2+ \
		  3
	print('Hello World!!')
	print(arrayss)
	print(total)
	if True:
		print('true')
		print('1')
	else:
		print('false')
		print('2')

class A:
	"这是类A的描述"
	def __init__(self,number):
		self.number=number
	"类A的方法display"
	def display(self):
		"类A的描述"
		print(" number = %d" % self.number)
		print(A.__doc__)

def inputFunction():
	print(sys.argv)
	#a=raw_input("按下 enter 键退出,其它任意键显示...\n")
	#print a

def typeTest():
	a = 1
	str1 = 'this is string 1'
	list1 = ['this', 'is', 'list', 2]
	tuple1 = ('this', 'is', 'tuple', 3)
	dict1 = {1:'this', 2:'is', 3:'dictionary', 4:4}
	print(a,type(a))
	print(str1,type(str1))
	print(list1,type(list1))
	print(tuple1,type(tuple1))
	print(dict1,type(dict1))
	if isinstance(a, int):
		print('true')
	else:
		print('false')
		print(isinstance(str1,str))

def aTest():
	t=A(123456)
	t.display()

def data2Json():
	# Python 字典类型转换为 JSON 对象
	data = {
		'no' : 1,
		'name' : 'Runoob',
		'url' : 'http://www.runoob.com'
	}
	# json.dumps(): 对数据进行编码。
	json_str = json.dumps(data)
	print ("Python 原始数据：", repr(data))
	print ("JSON 对象：", json_str)

def json2data():
	# Python 字典类型转换为 JSON 对象
	data1 = {
		'no' : 1,
		'name' : 'Runoob',
		'url' : 'http://www.runoob.com'
	}
	# json.dumps(): 对数据进行编码。
	json_str = json.dumps(data1)
	print ("Python 原始数据：", repr(data1))
	print ("JSON 对象：", json_str)
	# json.loads(): 对数据进行解码。
	# 将 JSON 对象转换为 Python 字典
	data2 = json.loads(json_str)
	print ("data2['name']: ", data2['name'])
	print ("data2['url']: ", data2['url'])

if __name__ == '__main__':
	# hello()
	# aTest()
	# typeTest()
	# data2Json()
	# json2data()
	# inputFunction()

	# domModule测试
	handler = domModule.MovieHandler('movies.xml')
	handler.parseXml()
"""
	# saxModule测试
	# 创建一个 XMLReader
	parser = xml.sax.make_parser()
	# turn off namepsaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	# 重写 ContextHandler
	Handler = saxModule.MovieHandler()
	parser.setContentHandler(Handler)
	parser.parse("movies.xml")
"""

