#### 클래스 구현 : 메서드, 필드 정의, 생성자 이용

# 클래스 선언
# class 클래스이름 [(슈퍼클래스명)]:

# # 빈 클래스 정의
# class Car:
#     pass
#
# car1 = Car()
# print(car1)
# # 객체 출력 <__main__.Car object at 0x00000140B448D1F0>

#
class Car:
    # 메소드 정의
    def show(self):
        print('시험중입니다')

# 인스턴스 생성
car1 = Car()
car2 = Car()
car3 = Car()
print('------------')
car1.show() # 메소드 호출
car2.show()
car3.show()

# 특정 클래스의 인스턴스인지 확인 : isinstance(인스턴스명, 클래스명)

print(isinstance(car1, Car)) # True 반환
print(isinstance(car1, int)) # False 반환

x = 3
print(isinstance(x,int)) # True 반환

y = list([1,2,3,4])
print(isinstance(y, list)) # True 반환

print(type(x))

z = 'Hi, 반가워요'
print(type(z))

a = True
print(type(a))

# 파이썬에서 기본제공하고 있는 int, float, str, bool, list, dict, set, tuple
# => 클래스

print(isinstance(a, int))

b = (1,2,3)
print(type(b))
print(isinstance(b, list))

# instance & object
# 같은 것 가리키고 있음
# instance : 클래스와 연관지어 말할 때
# 예). car1은 Car 클래스의 인스턴스이다
# object : 단독으로 부를 때
# 예) car1 객체

#######################################
# 필드 추가 : 메소드 내에서 사용

class Car:
    def show(self):
        print('시험중입니다')
    # def drive(self):
    #     self.speed = 60 # speed 필드
    #     print('%d'%self.speed)

#     def drive(self, speed):
#         self.speed = speed # speed 필드
#         print('%d' %self.speed)
# # 메인 : 인스턴스를 생성하고 이용
# car1 = Car()
# car1.drive(70)
# print(car1.speed)
# # car1.speed = 100
# car1.drive(50)
#
# # 인스턴스.필드
# car1.color = 'red'
# print(car1.color)
print('------------')

# class Car:
#     speed = 0
#     color = ''
#     def show(self):
#         print('시험중입니다')
#
#     def drive(self):
#         print('%d로 주행중입니다'%self.speed)
#
# mycar = Car()
# print(mycar.speed)
# mycar.drive()
# mycar.speed = 60
# mycar.drive()


# 생성자(consrutor) : 인스턴스를 생성해주는 함수

# 기본 생성자 : 인스턴스 호출 => 인스턴스명.클래스이름()
# class Car:
#     def __init__(self):
#         self.color = 'white'
#         self.speed = 0
#
#     def show_info(self):
#         print('이 자동차의 색상은 %s 입니다' %self.color)
#
#     def drive(self):
#         if self.speed != 0:
#             print('%d로 주행중입니다'%self.speed)
#         else:
#             print('정차중입니다')
#
# mycar = Car()
# print(mycar.color)
# print(mycar.speed)
# mycar.show_info()
# mycar.drive()
# mycar.speed = 50
# mycar.drive()

# 매개변수가 있는 생성자 __init__(self, 매개변수1, 매개변수 2...)
# 필드의 초기값 지정
# class Car:
#     def __init__(self,color,speed):
#         self.color = color
#         self.speed = speed
#
#     def show_info(self):
#         print('이 자동차의 색상은 %s 입니다' %self.color)
#
#     def drive(self):
#         if self.speed != 0:
#             print('%d로 주행중입니다'%self.speed)
#         else:
#             print('정차중입니다')
#
# mycar = Car('Red',100)
# print(mycar.color)
# print(mycar.speed)
# mycar.show_info()
# mycar.drive()
# mycar.speed = 50
# mycar.drive()
#
# yourcar = Car('Blue',0)
# yourcar.show_info()
# yourcar.drive()

# 디폴트 매개변수를 이용
# class Car:
#     def __init__(self,speed = 0,color = 'white'):
#         self.color = color
#         self.speed = speed
#
#     def show_info(self):
#         print('이 자동차의 색상은 %s 입니다' %self.color)
#
#     def drive(self):
#         if self.speed != 0:
#             print('%d로 주행중입니다'%self.speed)
#         else:
#             print('정차중입니다')
#
# car1 = Car()
# car2 = Car(color = 'Yellow')
# car3 = Car(10, 'Blue')
# car4 = Car(10)
# car1.show_info()
# car2.show_info()
# car3.show_info()
# car4.drive()
# car4.show_info()

# 비공개 필드
# 클래스 내부의 메소드를 통해서 사용
class Car:
    def __init__(self,speed = 0,color = 'white'):
        self.__color = color # 클래스 내에서만 사용하는 비공개 필드
        self.speed = speed

    # def __str__(self):

    # color 필드 값을 반환
    def getColor(self):
        return self.__color
    # color 필드값을 변경하는 메소드
    def setColor(self,color):
        self.__color = color

    # 비공개 메소드
    def __showColor(self):
        print('이 자동차의 색상은 %s 입니다'%self.__color)

    def show_info(self):
        self.__showColor()
        print('속도는 %d 입니다'%self.speed)

    def drive(self):
        if self.speed != 0:
            print('%d로 주행중입니다'%self.speed)
        else:
            print('정차중입니다')

    def upSpeed(self, up):
        self.speed += up
    def downSpeed(self,down):
        if self.speed > 0 :
            self.speed -= down
        else:
            self.speed = 0

car1 = Car()
print(car1.getColor())
car1.setColor('Red')
print(car1.getColor())
# car1.color = 'blue' # 필드를 외부에 직접 접근
# car1.__showColor()
car1.show_info()
car1.upSpeed(20)
car1.drive()
car1.upSpeed(20)
car1.drive()
car1.downSpeed(10)
car1.drive()