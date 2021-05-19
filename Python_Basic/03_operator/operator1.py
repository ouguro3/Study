# 산술연산자 : +, -, *, /, //, %, **

# 문제. 10000초는 몇시간 몇분 몇초인가?
s = 10000
m = s // 60
r = s % 60
h = m // 60

print("%d분 %d초" %(m, r))

# 산술연산자 우선 순위 :
#   ( )
#   지수**,
#   곱셈, 나눗셈, 나머지, 몫
#   덧셈, 뺄셈

# 할당연산자 : =
# 대입연산자 : +=, -=, *=, /=, //=, %=, **=
a = 100
a = a + 10      # a += 10
a = a + 10
a = a + 10

sum = 1
sum = sum + 2     # 1 + 2
sum = sum + 3     # 1 + 2 + 3
sum = sum + 4     # 1 + 2 + 3 + 4
sum = sum + 5     # 1 + 2 + 3 + 4 + 5


b -= 10   # b=b-10
c *= 100  # c=c*100
d /= 10   # d=d/10
e **= 3    # e=e**3


# 관계연산자 : > , < , >= , <=, ==, !=   => 결과값이 참(True), 거짓(False)

print(100 > 3)   # True
a = 100
b = 1001
print(a>b)
print(a!=b)

# 논리연산자  :  and, or, not
print('# 논리연산자')
print(a > b and b==1001) # False
print(a > b or b==1001)  # True
print(not(a>b))


# 비트연산자  : 정수를 2진수로 변환한 수 각각의 비트별로 연산
# &(논리곱), |(논리합), ^(xor), ~ (부정 not), << (왼쪽시프트), >>(오른쪽시프트)
print(10 & 3)    # 1010 & 0011 => 0010
print(10 | 3)    # 1010 | 0011 => 1011   (11)
print(10 ^ 3)    # 1010 ^ 0011 => 1001   (9)
print(~3)    # ~ 0011 => 1100   (12)
print(~3+1)

print(10<<1)
print(10<<2)
print(10<<3)

print(10>>1)
print(10>>2)
print(10>>3)

print('잔액 : ', format(1235000, ',.0f'))
print('잔액 : ', format(1235000, ',d'))
print('잔액 : ', format(1235000.123, ',.1f'))

