# 함수의 매개변수 형식
# 매개변수에 기본값 지정 : default parameter

# def showMessage(message='Hi'):
#     print(message)
#
# # defalut argument는 맨 뒤에
# def showMessage2(name, message='Hello!'):
#     print(name, message)



# showMessage('Hello')
# showMessage('Hi')
# showMessage('We are Happy!')
# showMessage2('Kim','Hi')
# showMessage2('Kim')
# showMessage()

#
def showNames(names):
    for name in names:
        print(name,end=' ')
    print()

names = (['Hong','Park','Choi','Lee'])
showNames(names)

# 함수의 실인수로 딕셔너리가 전달
def showInfoStd(student):
    print(student)
    print('이름 :',student['name'])
    print('나이 :',student['age'])
    print('연락처 :', student.get('phone'))

info_std = {'name':'kim', 'age':19, 'phone':'010-5061-1657'}
showInfoStd(info_std)

# 가변길이 매개변수
# *args : argument 1개 이상 지정
# *kwargs : keword arguments key = value

def mySum(*args):
    total = 0
    for x in args:
        total += x
    return total

def myShowInfo(**kwargs):
    for key in kwargs.keys():
        print(key, end=' ')
    print()
    for value in kwargs.values():
        print(value, end=' ')
    print()
    for item in kwargs.items():
        print(item)

# print(mySum(1,3,5))
# print(mySum(3,4))
# print(mySum(1,2,4,5,6))
# print(mySum([1,2,4,5,6]))

myShowInfo(id = 123, name='Kim', add='Seoul')
myShowInfo(id = 333, name='Lee')
myShowInfo(id = 123, name='Hong', add='Deagu', phone ='111-1111')

def calculator(operator, *args):
    pass

def studentInfo(name, age=10, sex='F'):
    student = {'name':name,
               'age':age,
               'sex':sex
               }
    return student

studentInfo('Lee', 30, 'F')
print(studentInfo(name='Kim', age=30, sex='M'))
print(studentInfo(name='Kim', sex='M', age=15))
# 위치인수와 키워드인수를 혼용할때는 키워드 인수는 위치인수의 뒤쪽으로

