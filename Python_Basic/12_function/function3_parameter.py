# 함수의 매개변수(parameter)
# 함수에 전달(입력)되는 값 (함수 정의할 때)

# 인수(argument) : 함수에 실제로 전달되는 값

# def showInfo(name, age):
#     print('이름은 %s이고 나이는 %d에요'%(name, age))
#
# showInfo('홍길동', 18)

# def getArea(width,height):
#     return width*height*0.5
#
# w = int(input('밑변 :'))
# h = int(input('높이 :'))
# print(getArea(w,h))

# 사칙연산을 수행하는 함수들을 정의하여 호출

# add(x,y)
# sub(x,y)
# mul(x,y)
# div(x,y)

# 2개의 숫자를 키보드로 입력받고, 각 함수에 전달하여
# 계산 결과를 아래와 같이 출력하는 코드 완성

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return  x * y
def div(x,y):
    return x / y

num1 = int(input('숫자 1:'))
num2 = int(input('숫자 2:'))
print(num1,'+',num2,'=',add(num1,num2))
print(num1,'-',num2,'=',sub(num1,num2))
print(num1,'x',num2,'=',mul(num1,num2))
print(num1,'/',num2,'=',div(num1,num2))