#/usr/bin/python
#coding=utf-8

a = 1
str1 = 'this is string 1'
list1 = ['this', 'is', 'list', 2]
tuple1 = ('this', 'is', 'tuple', 3)
dict1 = {1:'this', 2:'is', 3:'dictionary', 4:4}

print a,type(a)
print str1,type(str1)
print list1,type(list1)
print tuple1,type(tuple1)
print dict1,type(dict1)

if isinstance(a, int):
	print 'true'
else:
	print 'false'
print isinstance(str1,str)
