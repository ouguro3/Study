
def plus(a,b):
    c = a + b
    print(f'{a} + {b} = {c}')

def subtrack(a,b):
    c = a - b
    print(f'{a} - {b} = {c}')

def division(a,b):
    c = a / b
    print(f'{a} / {b} = {c}')

def multiply(a,b):
    c = a * b
    print(f'{a} X {b} = {c}')
    
print("사칙연산 계산 프로그램 시작")
while True:
    print("=" * 20)
    print("1. 더하기")
    print("2. 빼기")
    print("3. 나누기")
    print("4. 곱하기")
    print("5. 프로그램 종료")
    print("=" * 20)
    num = int(input("번호 입력 :"))
    if num == 1:
        print("=" * 20)
        print("더하기")
        print("=" * 20)
        a = int(input("첫번째 숫자 입력 :"))
        b = int(input("두번째 숫자 입력 :"))
        plus(a,b)
    elif num == 2:
        print("=" * 20)
        print("빼기")
        print("=" * 20)
        a = int(input("첫번째 숫자 입력 :"))
        b = int(input("두번째 숫자 입력 :"))
        subtrack(a,b)
    elif num == 3:
        print("=" * 20)
        print("나누기")
        print("=" * 20)
        a = int(input("첫번째 숫자 입력 :"))
        b = int(input("두번째 숫자 입력 :"))
        division(a,b)
    elif num == 4:
        print("=" * 20)
        print("곱하기")
        print("=" * 20)
        a = int(input("첫번째 숫자 입력 :"))
        b = int(input("두번째 숫자 입력 :"))
        multiply(a,b)
    elif num == 5:
        print("=" * 20)
        print("프로그램 종료")
        break
