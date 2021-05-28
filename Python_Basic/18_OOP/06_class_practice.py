# 클래스 상속 실습
# 슈퍼클래스 : 사람 클래스 Person <- 학생 클래스 Student

class Person:
    def __init__(self,age,name,sex):
        self.age = age
        self.name = name
        self.sex = sex

    def showInfo(self):
        print('이름 : %s , 나이 : %d, 성별 : %s'%(self.name,self.age,self.sex))


class Student(Person):
    # 학교, 학과, 학번, 공부하다(), 시험보다()
    def __init__(self,age,name,sex,school,dep,num):
        super().__init__(age,name,sex)
        self.school = school
        self.dep = dep
        self.num = num

    def test(self):
        print('%s이/가 시험보는 중입니다'%self.name)
    def study(self):
        print('%s이/가 공부 중입니다'%self.name)
    def greeting(self):
        print('안녕하세요 저는 %s 입니다 %s에 다니고 있고 %s를 배우고있습니다'%(self.name,self.school,self.dep))
        print('학번은 %s입니다'%self.num)

person1 = Student(22,'Lee','남','서울대','소프트웨어','123456')
person2 = Student(24,'Park','남','서울대','경제학','123456')
person3 = Student(22,'Choi','남','서울대','경영학','123456')
person1.greeting()
person1.test()

