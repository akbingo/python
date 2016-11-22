#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("tuple")
print(("S1"))
print(("S1",),"\n")

print("条件判断")
height=1.75
weight=80.5
BMI=weight/(height*height)
print("你的BMI是",BMI)
if BMI<18.5:
    print("过轻")
elif BMI<25:
    print("正常")
elif BMI<28:
    print("过重")
elif BMI<32:
    print("肥胖")
else:
    print("严重肥胖")
print("\n")

print("循环")
sum=0
x=1
while x<100:
    sum=sum+x
    x=x+2
print(sum)

sum=0
x=1
while x<100:
    x=x+2
    sum=sum+x
print(sum,"\n")

print("调用函数")
for x in (255,1000):
    print(hex(x))
print("\n")

print("定义函数")
import math
def quadratic(a,b,c):
    if a==0:
        return (-c)/b
    if a != 0:
        s=b*b-4*a*c
        if s>0:
            return (-b+math.sqrt(s))/(2*a),(-b-math.sqrt(s))/(2*a)
        elif s==0:
            return (-b)/(2*a)
        else:
            pass
print(quadratic(2,3,1))
print(quadratic(1,3,-4),"\n")

#汉诺塔的移动
print("递归函数")
def move(n,a,b,c):
    if n==1:
        print(a,"-->",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
    return "\t"
print(move(3,"A","B","C"))

print("列表生成式")
L1=["IBM","iPhone",69,"Hello",None]
print([l.lower()  for l in L1  if isinstance(l,str)==True])
print([l.lower  for l in L1  if isinstance(l,str)==True],"\n")

#杨辉三角
print("生成器")
def triangles():
    a=[1]
    while True:
        yield a
        v=[0]+a[:]
        a=[a[x]+v[x]  for x in range(len(a))]+[1]
        
x=0
for n in triangles():
    print(n)
    x=x+1
    if x==10:
        break
print("\t")

print("高阶函数:map/reduce")
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
L1=["adam","LISA","barT"]
def normalize(name):
    return name.title()
print(list(map(normalize,L1)))
#编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
    return reduce(akb,L)
def akb(x,y):
    return x*y
print("3*5*7*9=",prod([3,5,7,9]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    pass
print("\t")

print("高阶函数:filter")
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
print(list(filter(lambda n : str(n)==str(n)[::-1],range(1,1000))),"\n")
