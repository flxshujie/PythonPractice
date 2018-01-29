#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
'''


def trim(string):
	if len(string)==0:
		return string
	while string[0]==' ':
		if len(string)==1:
			return ''
		else:
			string = string[1:]
	while string[-1]==' ':
		string = string[:len(string)-1]
		
	return string
def trim2(s): 
	if len(s) == 0: 
		return s #长度为0，直接返回 
	while s[0] == ' ': #把前面的0都去掉了 
		if len(s) == 1: 
			return '' #当只有一个空字符时，下标1溢出，这里单独考虑 
		else: 
			s = s[1:]
	while s[-1] == ' ': #把后面的0都去掉了 
		s = s[:len(s) - 1] 
	return s

def trim3(s):
	if len(s)==0:
		return ''
	if s[0]==' ':
		return trim3(s[1:])
	elif s[-1]==' ':
		return trim3(s[:len(s)-1])
	else :
		return s

def trim4(s):
	if type(s)==str:
		while s[:1] ==' ':
			s=s[1:]
		while s[-1:] == ' ':
			s=s[:-1]
	return s

def trim5(s):
	if len(s)==0:
		return ''
	temp=s
	start = 0
	end = len(s)
	while s[0]==' ':
		if len(s)==1:
			return ''
		else:
			s=s[1:]
			start=start+1
	while s[-1]==' ':
		s=s[:len(s)-1]
		end = end-1
	if start == end:
		return ''
	return temp[start:end]

if trim5('hello  ') != 'hello':
    print('测试失败1!')
elif trim5('  hello') != 'hello':
    print('测试失败2!')
elif trim5('  hello  ') != 'hello':
    print('测试失败3!')
elif trim5('  hello  world  ') != 'hello  world':
    print('测试失败5!')
elif trim5('') != '':
    print('测试失败5!')
elif trim5('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')
print(trim5('  hello'))


