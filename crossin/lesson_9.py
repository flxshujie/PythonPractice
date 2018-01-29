from random import randint
num = randint(0,100)
bingo =False
print('what number do I think')

while bingo == False:
    answer = input()
    if answer < num :
        print ('%d is too small' %answer)
    elif answer >num :
        print ('%d is too big' %answer)
    else: 
        bingo =True
        print ('bingo,%d is the right answer' %answer)

for i in range(0,5):
    for j in range(0,i+1):
        print '*',
    print'\n'

