#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# filename: 0-python.py

"""
这是一个python实例文件
作者：Guile Liao
......
"""

__author__ = 'Guile Liao'                           #这个变量声明了程序作者

#def funMyFunction(): #定义函数
#       xxx;
#       xxx;
#funMyFunction end

import os                                           #导入os模块
import sys                                          #导入sys模块

strMyVar = "abc"                                    #定义变量字符串
numMyNum = 123                                      #定义变量数字
lisMyList = [                                       #定义列表（数组）
                'a',
                2.20,
                'c'
]
tupMyTuple = (                                      #定义元祖（只读列表）
                't0',
                't1',
                't2'
)
dicMyDict = {                                       #定义字典（键值对）
                't0': 'a',
                't1': 'b',
                't2': 3
}

def funMyPrint(args):
        print("\033[32m%s\033[0m" %(args));
        return
#funMyPrint end

for i in range(3):                                   #for循环（有限循环）
        funMyPrint(raw_input("请输入一个字符串："));
        funMyPrint(os.getcwd());
        funMyPrint(sys.platform);
        funMyPrint(sys.path);
        funMyPrint(lisMyList[i] * 2);
        funMyPrint(tupMyTuple[i] * 2);
        funMyPrint(dicMyDict[tupMyTuple[i]]);
