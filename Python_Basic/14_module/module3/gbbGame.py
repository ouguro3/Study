from random import randint

def gbb_game(you_n):
    com = randint(1,3)
    if com - you_n == -2 or com - you_n == 1:
        print('컴퓨터가 이겼습니다')
    elif you_n - com == -2 or you_n - com == 1:
        print('당신이 이겼습니다')
    elif com == you_n:
        print('비겼습니다')
    print('COM : %d'%com)

def input_num():
    num = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
    gbb_game(num)



