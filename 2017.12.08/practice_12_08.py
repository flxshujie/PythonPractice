# -*- coding: utf-8 -*-
import math
def abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError( "typeError shujie")
	if x>=0:
		return x
	else:
		return -x

def power(x,n):
	if not isinstance(x,int):
		raise TypeError("Type Error,shujie")
	result =1 
	while n>0:
	      result =x*result
	      n=n-1
	return result

def quadratic(a, b, c):
	deta = math.pow(b,2) - 4*a*c
	x1 = (-b+deta)/(2*a)
	x2 = (-b-deta)/(2*a)
	return x1,x2

def calc(*number):
	sum=0
	for n in number:
		sum = sum + math.pow(n,2)
	return sum
	
print("abs -9 is %d"%(abs(-9)))
print("power(5,3) is %d"%(power(5,3)))
x,y = quadratic(1, 3, 2)
print("x,y is %d, %d"%(x,y))
print("calc(1,2,3,4,5) is %d"%(calc(1,2,3,4,5)))
