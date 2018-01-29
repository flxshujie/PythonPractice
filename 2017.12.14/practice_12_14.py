# -*- coding: utf-8 -*-
from functools import reduce
def add(A , B ,f):
	return f(A)+f(B)

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
	if len(name)==0:
		return none
	return name.capitalize()

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def product(A,B):
	return A*B
def prod(L):
	if len(L)==0:
		return none
	return reduce(product,L)

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2int(s):
	digits={'1':1, '2':2, '3':3, '4':4, '5':5, '6':6}
	return digits[s]
def str2float(s):
	def fun(x,y):
		return 10*x+y
	n = s.index('.')
	left = s[:n]
	right = s[n+1:]
	leftnum =reduce(fun, map(str2int, left))
	rightnum=reduce(fun, map(str2int, right))
	
	return leftnum+rightnum%1000

print( add(-5,9,abs))
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
