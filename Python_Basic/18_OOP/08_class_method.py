# 클래스메소드(class method) : self를 통하지않고 바로 클래스가 메소드 호출
# @classmethod : 클래스 메소드임을 표시

class Person:
    count = 0 # 클래스 변수

    def __init__(self,name):
        Person.count += 1
        self.name = name
    @classmethod
    def showCount(cls):
        print('%d명 태어났습니다'%cls.count) # cls로 클래스 속성에 접근

    def greeting(self):
        print('%s가 인사해요' %self.name)

Kim = Person('Kim')
Person.showCount()
Lee = Person('Lee')
Person.showCount()
Kim.greeting()
Lee.greeting()
