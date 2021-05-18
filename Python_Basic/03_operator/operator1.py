# 산술 연산자 : +, -, *, /, //, %, **

# 문제. 10000초는 몇시간 몇분 몇초인가?

a = 10000
h = a // 3600
m = a//60 % 60
s = a % 60

print('%d시 %d분 %d초'%(h,m,s))



# 할당 연산자 : =


# 대입 연산자 : +=, -=, *=, /=, //=, %=, **=

b = 1

b += 1
print(b)

b *= 2
print(b)

# 관계 연산자 : >, <, >=, <=, ==, !=    결과값이 참(True), 거짓(False)

print(100 > 3)  # True
a = 100
b = 1001
print(a>b) # False
print(a!=b) # True

# 논리 연산자 : and, or, not

print(a > b and b==1001) # False
print(a > b or b==1001) # True
print(not(a>b)) #True

# 비트 연산자 : 정수를 2진수로 변환한 수 각각의 비트별로 연산
#  &(논리곱), |(논리합), ^(xor), ~(부정 not), << (왼쪽 시프트), >> (오른쪽 시프트)

print(10 & 3)
print(10 | 3)
print(10 ^ 3)
print(~3)
print(~3+1)

print(10<<1)
print(10<<2)
print(10<<3)


