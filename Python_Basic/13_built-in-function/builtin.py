# enumerate(iterable, start = 0)
# 시퀸스 (리스트, 튜플, 문자열, range)를 인덱스 값을 포함하는 enumerate 객체로 반환

enum = enumerate(['apple','banana','melon','strawberry','kiwi','watermelon'])
print(enum)

for i, item in enum:
    print(i, item)


seasons = ['Spring','Summer','Fall','winter']
enumSeason = list(enumerate(seasons, start=1))
print(enumSeason)

# eval()
print(eval('3.1'))
print(eval('10+100'))

# filter(function, iterable) : 반복가능한 자료형 요소에 함수를 적용하여
# 반환값이 참(True)인 결과만 걸러내어 반환

def positive(x):
    return x > 0

print(positive(-9))

result = filter(positive, [-10,0,3,-8,7])
print(type(result))
print(list(result))

# 실습문제 : 짝수인지를 판별하는 함수 even(x)를 정의하고,
# 이 함수를 filter를 이용하여 주어진 리스트의 짝수만 걸러내는 코드

# def even(x):
#     if x % 2 == 0:
#         return x
#
# list1 = []
# for i in range(5):
#     num = int(input('숫자 입력 :'))
#     list1.append(num)
# result = filter(even, list1)
# print(list(result))

# list()
list('Hi Hello')

# sorted(iterable, key = None, reverse=True)
print(sorted([10,-4,5]))
print(sorted([10,-4,5], reverse=True))
print(sorted('flower'))
print(sorted('SunFlower', key=str.lower))

# range()
print(type(range(5)))
print(list(range(5)))
print(list(range(2,10,3)))
print(tuple(range(5)))

# zip(*iterable) : 각 iterable에서 동일한 인덱스 요소를 추출하여 묶어서 변환

print(zip([1,3,5], ['cat','dog','house']))
print(list(zip([1,3,5], ['cat','dog','house'])))
print(list(zip([1,3,5], ['cat','dog','house','lion'])))
print(tuple(zip([1,3,5], ['cat','dog','house'])))

keys = ['cat','dog','horse']
values = [1,3,5]
result = dict(zip(keys, values))
print(result)

# map()

result = list(map(str, range(10)))
print(result)
print(list(map(int, result)))

