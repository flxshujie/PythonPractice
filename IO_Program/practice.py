#-*- coding: UTF-8 -*- 

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
import os
import time

def eachFile(filePath):
    pathdir =os.listdir(filePath)
    for alldir in pathdir:
        child = os.path.join(filePath, alldir)
        print(child)

def readFile(filePath):
    pathdir =os.listdir(filePath)
    for alldir in pathdir:
        child = os.path.join(filePath, alldir)
        if os.path.isfile(child): 
        	wfopen = open("content.txt",'w')
		fopen = open(child ,'r')
        	for eachline in fopen:
            		print("THE CONTENT IS:", eachline)
			wfopen.write(eachline)
        	fopen.close()
		wfopen.close()

def changeName(fileName):
	if not os.path.isdir(fileName) and not os.path.isfile(fileName):
		return False
	global i
	if os.path.isfile(fileName):
        	pathName = os.path.split(fileName)
		lists = pathName[1].split('.')
		suffix = lists[-1]
		if suffix in ['jpg','bmp','jpeg','gif','psd','png']:
			suffix = '_fc.' + suffix
			os.rename(fileName,pathName[0]+'/'+lists[0]+suffix)
			i +=1
	elif os.path.isdir(fileName):
		for x in os.listdir(fileName):
			changeName(os.path.join(fileName,x))
#eachFile(os.getcwd())
#readFile(os.getcwd())
i = 0
print('the start time is:')
start = time.time()
changeName(os.getcwd())
end   = time.time()
print start
print('the duration time is %d:',end -start)
print('the avg time to process image is:', (end-start)/i)
print(i)
