#!/usr/bin/python
 
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    print(b,end=',')
    print(a,b,sep='|')
    a, b = b, a+b
