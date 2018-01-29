# -*- coding: utf-8 -*-
import time, functools
'''
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
'''
def log(func):
    @functools.wraps(func)
    def metric(*args,**kw):
	localtime2 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        s_time=time.time()
        r = func(*args,**kw)
        e_time=time.time()
        localtime1 = e_time - s_time
        print('%s execute in %s ms in %s' %(func.__name__,localtime1,localtime2))
        return func(*args,**kw)
    return metric
# 测试
#@metric
@log
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

#@metric
@log
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
