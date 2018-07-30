# r.py
import sys,getopt

#递归算法 填充斐波拉契数列
x,y=0,1
f_len,f_max=[],[]
f_len.append(x);f_len.append(y)
f_max.append(x);f_max.append(y)

#按最大个数填充
def Fsqe_Len(n):
    if len(f_len)<n:
        Fsqe_Len(n-1)
    m=f_len[n-1]+f_len[n-2]
    f_len.append(m)
    
#按最大值填充
def Fsqe_Max(fmx):
    fmlen=len(f_max)-1
    if f_max[fmlen]>fmx:
        del f_max[fmlen]
    else:
        m=f_max[fmlen-1]+f_max[fmlen]
        f_max.append(m)
        Fsqe_Max(fmx)
    
lens=int(input('Fsqe_Len 输入最大个数：'))
maxs=int(input('Fsqe_Max 输入最大值：'))
if __name__ == '__main__':
    Fsqe_Len(lens)
    Fsqe_Max(maxs)
    print(f_len)
    print(f_max)
