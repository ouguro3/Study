# 팩토리얼 계산 함수

# n != n*(n-1)*(n-2)*....*2*1

def factorial(n):
    ret = 1
    for i in range(n, 0, -1):
        ret *= i
    return ret
print(factorial(5))

# import math
#
# def fac(n):
#     a = math.factorial(n)
#     return a
#
# print(fac(5))