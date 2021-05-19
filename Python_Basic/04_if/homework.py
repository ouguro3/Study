# 연산자, if문을 이용한 프로그램 작성 문제

# 1. 16진수 구분
a = input('16진수 한 글자 입력 :')

if ('0' <= a <= '9') or ('A' <= a <= 'F') or ('a' <= a <= 'f'):
    print('10진수 ==> %s ',int('a',10))
else:
    print('16진수가 아닙니다')

print('='*20)

# 2. 입력한 금액 단위별 나누기
money = int(input('교환할 돈은 얼마? :'))

a = money // 50000
b = (money % 50000) // 10000
c = (money % 10000) // 5000
d = (money % 5000) // 1000
e = (money % 1000) // 500
f = (money % 500) // 100
g = (money % 100) // 50
h = (money % 50) // 10
money %= 10

print('5만원:%d장,만원:%d장,5천원:%d장,천원:%d장'%(a,b,c,d))
print('500원:%d개,100원:%d개,50원:%d개,10원:%d개'%(e,f,g,h))
print('남은 돈 --> %d'%money)

print('='*20)

# 3 주사위 게임
import random


a = random.randint(1,6)
b = random.randint(1,6)

print('A의 주사위 숫자는 %d 입니다'%a)
print('B의 주사위 숫자는 %d 입니다'%b)
if a > b:
    print('A가 이겼습니다')
elif a == b:
    print('비겼네용')
elif a < b:
    print('B가 이겼습니다')
