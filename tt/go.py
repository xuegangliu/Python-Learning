#!/usr/bin/python
# coding=utf-8

class A:
	"this is class A"
	def __init__(self,kk):
		self.kk=kk
	def display(self):
		print " aaaa %d" % self.kk

t=A(123)
t.display()
