#!/usr/bin/python
# coding=utf-8
# author: xuegangliu

import sys,os

'''
python import模块时， 是在sys.path里按顺序查找的。
sys.path是一个列表，里面以字符串的形式存储了许多路径。
'''
sys.path.append(os.path.abspath("./../../../"))

from org.lxg.test.threadModule import threadingModule

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


