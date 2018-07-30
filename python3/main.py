#/usr/bin/python3
'''
printOne
'''
def printOne(a):
  '''xxxxxxx'''
  print(a,'World.',end='\n')

"""
typeTwo name
"""
def typeTwo(a,b,c,d,e,f,g):
  '''this is typeTwo doc'''
  print(type(a))
  print(type(b))
  print(type(c))
  print(type(d))
  print(type(e))
  print(type(f))
  print(type(g))

def isK(t):
  if t==2:
    print('t==2')
  elif t==3:
    pass
  else:
    print('t!=2')

# this is llllllllll
a='Hello!'
t1,t2,t3=1,100.01,'ok'
t4=[1,2,3,4,5,'ddd',10.01]
t5=(1,2,3,4)
t6={'A','B'}
t7={'name':'lxg'}
k1=int(input('input number:'))

if __name__ == '__main__':
  printOne(a)
  typeTwo(t1,t2,t3,t4,t5,t6,t7)
  print(printOne.__doc__)
  print(1,2,3,sep='|')
  isK(k1)
