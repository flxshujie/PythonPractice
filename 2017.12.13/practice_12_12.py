def recursion(n):
	if n==1:
		return 1
	else: 
		return n*recursion(n-1)

def end_recursion(n):
	return end_def(n,1)

def end_def(n,m):
	if n==1:
		return m
	else:
		return end_def(n-1,n*m) 

def move(n,A,B,C):
	if n==1:
		print('move', A, '->', C)
	else:
		move(n-1, A, C, B)
		move(1, A, B, C)
		move(n-1, B, A, C)
	 
#print(recursion(10))
print(end_recursion(100))
print(move(64,'A','B','C'))
