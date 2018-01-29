from random import choice
print 'which side will you choice'
print 'left.right,middle?'
yourchoice = raw_input()
print 'your choice is %s' %yourchoice
direction = ['left','right','middle']
randomchoice = choice(direction)

if randomchoice == yourchoice:
     print 'congratuatios, goal'
else:
     print 'oops %s' %randomchoice
