# 첫번째 프로그램

# print('Lee Hyun Bum")

# 변수에 값을 저장(할당 assign)
x = 10
y = 20
z = 30
print(x,y,z)

# 여러개의 변수에 여러개의 값을 저장
x,y,z = 10,20,30
print(x,y,z)

# 여러 개의 변에 동일한 값을 할당
a=b=c=100
print(a,b,c)

# 두 변수의 값을 교환(swap)
a,b = 10,20
print('a =',a)
print('b =',b)

print('[swap]')

# 변수를 하나 더 지정하는 방법
c = a
a = b
b = c

# 파이썬의 swap 기능
a,b = b,a
print('a =',a)
print('b =',b)

# 변수를 삭제
x = 100
del x
print(x)

# 문자열에 큰 따옴표 사용
name = '이현범'
age = 32
print(name,age)

address = '경기도 평택시'
print(name + '은' + address + '에 삽니다' )

# str() : 숫자형을 문자열로 변환
print(name + '은' + str(age) + '살 입니다')
# + 를 사용할 때 문자열과 정수형 변수는 함께 사용이 불가능

# 형변환
# 값의 형태를 강제적으로 다른 형태로 변환하는 것
# 예) int -> str, str-> float
# 문자열 형변환 함수 str()
# 정수형 형변환 함수 str()
# 실수형 형변환 함수 str()
## 파이썬은 파일단위로 일괄 실행 시킨다.  가급적 콘솔 실행은 하지 말 것

# 사각형의 면적을 구하는 프로그램

width = 100
height = 50
area = width * height
print('사각형의 면적은', area)

# 실습 1.
name = '이현범'
no = 2016001
year = 4
grade = 'A'
average = 93.5

print('성명 : %s' % name)
print('학번 : %d' % no)
print('학년 : %d' % year)
print('성적 : %s' % grade)
print('평균 : %.1f' % average)

print('이름: %s, 학년: %d'%(name,year))
rate = 80
print('이름: %s, 출석률: %d'%(name,rate))

# 실습 2.
kor,eng,math = 90,80,80
total = kor+eng+math
aver = total / 3

print('총점 :{:d}, 평균 :{:.1f}'.format(total,aver))

# 화씨온도를 섭씨 온도로 변환하는 프로그램
# 화씨 -> 섭씨 변환 공식
# C = (F-32)*5/9
fTemp = 90
cTemp = (fTemp - 32) * 5 / 9
print(cTemp)

# 포맷코드 사용
print('%f' %cTemp) # 6자리로 소수점 이하 제한

# 소수점 이하 두자리수로 출력
print('%.2f'%cTemp)
# 소수점 이하 생략
print('%.f'%cTemp)

#----------------------------------------------
# tip : format() 함수 사용
# 소수점 이하 2자리 출력 함수 사용 예제
# 형식 : format(실수, '전체 자릿수, 소수 이하 자릿수<서식기호>')

print(format(cTemp, '10.2f'))
#    32.22 출력 >> 전체 자리수가 10이기 때문에 앞에 공백이 출력됨
# 소수점 이하 자리수를 제한하기 때문에 공백으로 채워진다.
# 소수점 포함해서 자리수 계산

#-------------------------------------------------
# 포맷코드 사용 2개 이상의값 출력
# 실제 출력되는 값들은 ()로 묶어야 한다
# print('%d %f" % (정수값, 실수값))

total = 250
average = 83.33
print("%d, %.2f" % (total,average)) #반드시 괄호로 묶는다.

# 상수
# 값이 변경되지 않는 값
# 파이썬에서는 별도의 상수가 없음
# 변수와 구분하기 위해 대문자로 사용
# 나중에 상수의 값을 변경해도 오류가 없음
# 프로그램 내에서 변하지 않는 값을 쓸때는 상수로 처리하는 것이 편하다.

PI = 3.141592 # 대문자 이름이므로 상수로 처리
r = 10
area = r*r*PI
print(area)

INT_RATE = 0.03
deposit = 10000
interest = deposit * INT_RATE
balance = deposit + interest

print(balance) # 변수값 그대로 출력
print(int(balance)) # 변수값을 정수형으로 변환하여 출력
print(format(int(balance),',')) # 변수값을 정수형으로 형 변환 후 천단위 구분자 기호

# 정수 리터럴
a = 0b1010 #2진수
b = 300
c =0o123 #8진수
d = 0x12fc #16진수
print(a, b, c, d)

#-------------------
#실수 리터럴
f1 = 3.14
f2 = -123.45
f3 =1.234567e5
print(f1,f2,f3)

#----------------
#문자열 리터럴
char1 = 'A'
char2 = "B"
print(char1,char2)

str1 ='홍길동'
str2 = "python"
str3 = """Python Programming"""
str3 = '''Python Programming'''

str4 = '''삼 따옴표는
여러줄에 나누어서
문자을 저장할 때 사용'''#enter까지 문자열로 저장

print(str4)

#논리값 리터럴
t = True
f = False

print(t,f)

#특수 리터럴
#None

address = None
print(address)
print(type(address))
print(id(address))


a = 1 + 2 + \
    4 + 5
print(a)

b = (1 + 2+
     3+5)
print(b)

print("c:\pythonStudy\name")
print(r"c:\pythonStudy\name")

print("first", end="@")
print("second")



#주석문
# 프로그램에 대한 설명문, 실행에 영향 없음

#주석처리 방법
# 1줄 주석 : 줄 맨 처음에 # 기호 사용
# 블럭 주석 : 파이썬은 여러줄 주석 기호는 없음. 다만, ''' ''' 이용하면
# 문자열 처리 되면서 실행에 영향을 주지 않는다
#
# 주석문을 미리 입력 해 농고 ctrl + / 키를 이용해 한번에 주석처리

# 주석을 사용하는 이유
# 프로그램에 관한 정보를 추가할 수 있다.
# 수정이 용이하다
# 가독성을 높여준다.
# 코드를 이해하기 쉽다
#
# 가능하면 코드에 주석을 붙이는 습관이 필요

#----------------------------------------
#행 분리 기호
# 1줄의 내용이 긴 경우 여러 행으로 분리 가능
# 역 슬래시나 괄호 사용

#역 슬래시 사용
# a = 1+2+3+ \
# 4+5+6

#괄호 사용
a = (1+2+3+
4+5+6)

#print 함수에서 여러 행으로 입력
#문자열 중간에서 엔터키를 치면 다음행으로 가고 자동을 ""처리되면서
#1줄로 인식

print("긴 문장을 입력할 때 중간에서 엔터키를 치면"
      "다음행으로 가고 자동으로 따옴표 처리 되면서"
      "1줄로 인식")

#여러줄로 출력 하려면 줄바꿈 문자(\n)  사용
print("긴 문장을 입력할 때 중간에서 엔터키를 치면\n"
      "다음행으로 가고 자동으로 따옴표 처리 되면서\n"
      "1줄로 인식")

#------------행결합
#2개의 문장을 한줄에 입력시 에러 발생
# print('apple') print('banana')

#행 결합해서 2개 문장을 한줄에 입력하기 위해 ; 을 추가
print('apple') ; print('banana')



#print() 함수 : 다음행으로 커서를 이동
print("first")
print("second")

#옆으로 출력(한줄에 모두 출력)
print("first", end="")
print("second")

#구분자 표시: 띄어쓰기, 쉼표, 대시, 콜론, ....
print("first", end="-")
print("second")

