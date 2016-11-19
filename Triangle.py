#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def triangles():
    a = [1];
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
        
n=0
for av in triangles():
    print(av)
    n=n+1
    if n==10:
        break
