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
sys.path.append(r'D:\WorkSpaces\Self\python\test\threadModule')

import json
import xml.dom.minidom
import xml.sax
import _thread

import threadModule
import threadingModule
import baseModule
import domModule
import saxModule

sumCount=1

if __name__ == '__main__':
	# threadingModule 创建新线程
	thread1 = threadingModule.myThread(1, "Thread-1", 1)
	thread2 = threadingModule.myThread(2, "Thread-2", 2)
	# 开启新线程
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
	print ("退出主线程")

'''
	# threadModule创建两个线程
	try:
		_thread.start_new_thread(threadModule.print_time,("Thread-1", 2, ))
		_thread.start_new_thread(threadModule.print_time,("Thread-2", 4, ))
	except:
		print ("Error: 无法启动线程")

	while sumCount<3:
		pass
'''
	# baseModule.hello()
	# baseModule.aTest()
	# baseModule.typeTest()
	# baseModule.data2Json()
	# baseModule.json2data()
	# baseModule.inputFunction()

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

