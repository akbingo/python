#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"这个模块可以生成一注双色球彩票。"

__author__=". ./akb"

import random
def akb():
    ske=[]
    while len(ske)<6:
        nmb=random.randint(1,33)
        hkt=0
        if len(ske)>=1:
            for av in range(len(ske)):
                if nmb==ske[av]:
                    hkt=1
        if hkt==0:
            ske.append(nmb)
    return sorted(ske)
if __name__=="__main__":
    print(akb(),"+",random.randint(1,16))