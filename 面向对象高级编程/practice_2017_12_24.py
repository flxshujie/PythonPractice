# -*- coding: utf-8 -*-

#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
	return self._width
    @width.setter
    def width(self, width):
	if not isinstance(width,int):
		raise TypeError
        self._width = width

    @property
    def height(self):
        return sefl._height
    @height.setter
    def height(self, height):
	if not isinstance(height,int):
		raise TypeError
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height
#定制类
#__str__
class Student(object):
	def __init__(self, name):
		self._name = name
	def __str__(self):
		return "Student object (name: %s)" %self._name
#__iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

print(Student("shujie"))
s=Student("shujie")

for n in Fib():
	print(n)
