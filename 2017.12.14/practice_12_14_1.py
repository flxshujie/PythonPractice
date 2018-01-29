# -*- coding: utf-8 -*-
from functools import reduce

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):					#嵌套一个函数，用来做乘法
	def func(x,y):
		return 10*x+y				#将输入的字符串在.分割，分别将左右两边的字符保存成数字形式
	num = s.index('.')
	left  = list(map(int,[x for x in s[:num]]))
	right = list(map(int,[x for x in s[num+1:]]))	#输出最后的结果
	return reduce(func,left)+reduce(func,right)/10.0**len(right)


#用filter求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() 					# 初始序列
    while True:
        n = next(it)					# 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) 		# 构造新序列



#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
	string = str(n)
	reverse = string[::-1]
	return string==reverse

#假设我们用一组tuple表示学生名字和成绩：L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)] 请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]
def by_score(t):
	return t[1]
# 测试:
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

'''
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
'''

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score, reverse = True)
print(L3)
