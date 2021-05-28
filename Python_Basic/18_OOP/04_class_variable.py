# 인스턴스 변수와 클래스 변수

class Car:
    number = 0
    def __init__(self):
        Car.number += 1


for i in range(1,8):
    car = Car()
    # 클래스 변수
    print(car.number)
    # car2 = Car()
    # print(car2.number)변수

