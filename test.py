#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("tuple")
print(("S1"))
print(("S1",),"\n")

print("条件判断")
height=1.75
weight=80.5
BMI=weight/(height*height)
if BMI<18.5:
    print("过轻")
elif 18.5<=BMI<25:
    print("正常")
elif 25<=BMI<28:
    print("过重")
elif 28<=BMI<32:
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
print([l.lower  for l in L1  if isinstance(l,str)==True])
