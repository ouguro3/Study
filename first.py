def gugunormal(n):
    print("=" * 20)
    print("%d 단 출력" %n)
    print("=" * 20)
    for j in range(2,10):
        print(f'{n} X {j} = {n*j}')

def guguvertical():
    for i in range(2,10):
        for j in range(2,10):
            print(f'{i} X {j} = {i*j}')

def guguhorizon():
    for i in range(2,10):
        for j in range(2,10):
            print(f'{j} X {i} = {j*i}', end='\t')

print("구구단 프로그램 시작")
while True:
    print('=' * 20)
    print("1. 특정 단수 출력")
    print('2. 구구단 세로 출력')
    print('3. 구구단 가로 출력')
    print('4. 프로그램 종료')
    print("=" * 20)
    print('입력 :', end='')
    num = int(input())
    if num == 1:
        n = int(input('단수를 입력하세요 :'))
        gugunormal(n)
    elif num == 2:
        guguvertical()
    elif num == 3:
        guguhorizon()
    elif num == 4:
        print("프로그램 종료")
        break
