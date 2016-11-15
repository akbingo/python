#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(("S1"))
print(("S1",))

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
print(sum)

for x in (255,1000):
    print(hex(x))
