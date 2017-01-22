#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"这个模块可以生成10组密码。"

__author__=". ./akb"

import random
import string
length=int(input("请输入你需要的密码位数："))
ske=input("请输入你需要的密码形式（如需要全数字则输入1，输入其它则是数字、大小写英文字母和特殊符号的密码形式）：")
def akb():
    if ske=="1":
        return ''.join([random.choice(string.digits) for av in range(length)])
    else:
        chrs=string.ascii_letters+string.digits+"!@#$%^&*()"
        return ''.join([random.choice(chrs) for av in range(length)])
if __name__=="__main__":
    for av in range(10):
        print(akb())
