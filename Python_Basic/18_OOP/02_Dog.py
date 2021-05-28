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

dog1 = Dog('진돗개','large',10,'yellow')
dog2 = Dog('말티즈','small',2,'white')
dog1.show_info()
print('--------')
dog2.show_info()
print('--------')
dog2.Eat()
dog2.sleep()
dog2.play()



