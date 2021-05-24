# 함수  >> 특정 작업을 수행하는 코드 집합

# 함수 예) print() input() type() 등등

# 메소드 >> 특정 객체를 통해 사용 가능한 함수
# .sort() .split()  .insert()  등등

# 함수 정의
def printHello():
    print('Hello')

def printName(name):
    print('name')

def area_sqaure(width, height):
    area = width * height
    return area

w = 10
h = 20

# 함수 호출
area = area_sqaure(w,h)
print(area)
printHello()
printName('Lee')

# 연습문제

# 자기 이름 : show_info()
# 나이
# 연락처
# 순서로 출력

def show_info():
    print('이현범')
    print('32')
    print('010-5061-1657')

show_info()

# 함수이름 sum()
# 숫자 2개를 키보드로 입력받아서 두 수의 합을 출력

# 숫자1 입력 : 10
# 숫자2 입력 : 20
# 합 : 7

def sum():
    a = int(input('숫자 1 입력 :'))
    b = int(input('숫자 2 입력 :'))
    to = a + b
    print(to)

sum()
