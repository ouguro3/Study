# 1)
for i in range(5):
    for j in range(i,5):
        print('*',end='')
    print()

print('='*20,end='\n')

# 2)
for i in range(1,6):
    for j in range(6-i):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()

print('='*20,end='\n')

# 3) 7 입력 시 종료되는 코드
while True:
    a = int(input('숫자 입력 :'))
    if a == 7:
        break
    elif a != 7:
        int(input('다시 입력 :'))

print('7 입력! 종료')

print('='*20,end='\n')

# 4) 1곡에 2000원 하는 노래방 기계에서 잔액이 소진될 때까지 노래방을 이용하는 프로그램
n = 0
m = 10000
while True:
    n += 1
    print('노래를 %d곡 불렀습니다'%n)
    m -= 2000
    print('현재 %d원 남았습니다'%m)
    if m == 0:
        break
print('잔액이 없습니다.  종료합니다')