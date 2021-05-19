# 컴퓨터와 게임하는 경우
from random import randint

compNum = randint(1, 100)
myNum = randint(1, 100)
print('com : %d vs my : %d' %(compNum, myNum))
if(myNum > compNum):
    print('성공')
else:
    print('실패')

