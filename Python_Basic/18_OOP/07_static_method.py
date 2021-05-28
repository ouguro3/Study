# 정적 메소드(static method)
# @staticmethod : 함수의 데코레이터 -> 정적 메소드로 정의한다 표시

class Calc:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a, b):
        return a - b

print(Calc.add(10,5))
