# 클래스 상속

class Dog:
    def __init__(self,breed,size,age,color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def show_info(self):
        print('견종 = %s,\n사이즈 = %s,\n나이 = %d,\n색 = %s'%(self.breed,
                                                          self.size,
                                                          self.age,
                                                          self.color))

    def Eat(self):
        print('%s가 음식을 먹는다'%self.breed)
    def sleep(self):
        print('%s가 잠들었다'%self.breed)
    def play(self):
        print('%s가 놀고있다'%self.breed)

class DogNum(Dog):
    def __init__(self,breed,size,age,color,name):
        super().__init__(breed,size,age,color)
        self.name = name

    def __str__(self):
        return '이름 = %s , 나이 = %d살 , 종류 = %s'%(self.name,self.age,self.breed)
    def __lt__(self, other):
        return self.age < other.age
    def __eq__(self, other):
        return self.age == other.age


dog1 = DogNum('진돗개','large',10,'yellow','진돌이')
dog2 = DogNum('말티즈','small',2,'white','크림이')
dog3 = DogNum('푸들','large',10,'brown','범군이')

print(dog1)
print(dog2)
print(dog3)
if dog2 < dog1:
    print('%s가 나이가 적네요'%dog2.name)
if dog3 == dog1:
    print('%s와 %s는 나이가 같습니다'%(dog3.name,dog1.name))


