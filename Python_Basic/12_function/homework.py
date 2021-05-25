# 1. '비트코인' 문자열을 출력하는 print_coin() 함수를 정의
def print_coin():
    print('비트코인')

# 2. 1번에서 정의한 함수를 호출
print_coin()

# 3. 1번에서 정의한 함수를 100번 호출
num = 0
for i in range(100):
    num += 1
    print('%d 번 호출'%num)
    print_coin()

# 4. '비트코인' 문자열을 100번 출력하는 함수를 정의
def print_coin():
    num = 0
    for i in range(100):
        num += 1
        print('비트코인 %d번째 출력'%num)
print_coin()

# 5. 아래의 에러가 발생하는 이유
# hello()
# def hello():
#     print('Hi')
# 함수의 호출이 함수의 생성보다 먼저 실행되어서

print('-'*20)
# 6. 아래 코드의 실행 결과 예측
def message():
    print('A')
    print('B')
message()
print('C')
message()

# A B C A B

print('-'*20)

# 7. 아래 코드의 실행결과 예측
print('A')
def message():
    print('B')
print('A')
print('C')
message()

# A A C B

print('-'*20)

# 8. 아래 코드의 실행결과 예측
print('A')
def message1():
    print('B')
print('C')
def message2():
    print('D')
message1()
print('E')
message2()

# A C B E D

print('-'*20)

# 9. 아래 코드의 실행 결과를 예측
def message1():
  print("A")
def message2():
  print("B")
  message1()
message2()

# B A

print('-'*20)

# 10. 아래 코드의 실행결과 예측
def message1():
    print('A')
def message2():
    print('B')

def message3():
    for i in range(3):
        message2()
        print('C')
    message1()
message3()

# B C B C B C A

print('-'*20)

# 11. 두 수를 입력 받아서 곱셈값을 리턴하는 함수를 작성
def mul():
    x = int(input('첫번째 수 :'))
    y = int(input('두번째 수 :'))
    mul = x * y
    return mul
print(mul())

print('-'*20)

# 12 . 소문자로 작성된 ticker를 입력 받은 후 이를 대문자로 변환된 ticker를 리턴하는 함수 작성
def up():
    a1 = input('입력 :')
    a1 = a1.upper()
    return a1
print(up())

# def up(x):
#     x = x.upper()
#     return x
# word = input('입력 :')
# print(up(word))

print('-'*20)

# 13. 함수로 인자로 리스트를 입력 받은 후 해당 리스트에서 짝수만 모아서 리턴하는 pickup_even() 함수를 작성
def pickup_even(x):
    list1 = []
    for i in x:
        if i % 2 == 0:
            list1.append(i)
    return list1


a = [1,2,3,4,5,6,7,8,9,10]
print(pickup_even(a))


