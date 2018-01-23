#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# filename: 0-python.py

"""
这是一个python实例文件
作者：Guile Liao
......
"""

__author__ = 'Guile Liao'       #这个变量声明了程序作者

#def funMyFunction():
#       xxx;
#       xxx;
#funMyFunction end

import os
import sys

strMyVar = "abc"
numMyNum = 123
lisMyList = [
                'a',
                2.20,
                'c'
]
tupMyTuple = (
                't0',
                't1',
                't2'
)
dicMyDict = {
                't0': 'a',
                't1': 'b',
                't2': 3
}

def funMyPrint(args):
        print("\033[32m%s\033[0m" %(args));
        return
#funMyPrint end

for i in range(3):
        funMyPrint(os.getcwd());        #("/"+raw_input("请输入一个字符串：")));
        funMyPrint(sys.platform);
        funMyPrint(sys.path);
        funMyPrint(lisMyList[i] * 2);
        funMyPrint(tupMyTuple[i] * 2);
        funMyPrint(dicMyDict[tupMyTuple[i]]);
