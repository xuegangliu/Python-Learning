#!/usr/bin/python
# coding=utf-8
# author: xuegangliu

import sys
'''
python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
'''
sys.path.append(r'D:\WorkSpaces\Self\python\test\xmlModule')
sys.path.append(r'D:\WorkSpaces\Self\python\test\baseModule')

import json
import xml.dom.minidom
import xml.sax

import baseModule
import domModule
import saxModule

if __name__ == '__main__':
	baseModule.hello()
	baseModule.aTest()
	baseModule.typeTest()
	baseModule.data2Json()
	baseModule.json2data()
	baseModule.inputFunction()

	# domModule测试
	# handler = domModule.MovieHandler('movies.xml')
	# handler.parseXml()

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

