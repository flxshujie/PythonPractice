#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from collections import Iterable
def findMinAndMax(L):
	if not isinstance(L,Iterable):
		return '不可迭代类型'
	elif len(L)==0:
		return (None,None)
	else:	
		mini=L[0]
		maxu=L[0]
		for i in L:
			if i<mini:
				mini=i
			if i>maxu:
				maxu=i
		return (mini,maxu)

def outputList(L):
	return [d.lower() for d in L if isinstance(d,str)==True]

#杨辉三角把每一行看做一个list，试写一个generator，不断输出下一行的list
def triangles():
    L=[1]
    while True:
        yield L
        L=[L[i]+L[i+1] for i in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

L1 = ['Hello', 'World', 18, 'Apple', None]
# 测试
L2=outputList(L1)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
    print(L2)

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
