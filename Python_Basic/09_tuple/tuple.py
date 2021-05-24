# 집합적 자료형 : tuple
# 삭제, 변경, 추가 작업불가

# 리스트 생성 : list() or []
# tuple 생성 : tuple() or ()

t1 = tuple()
t2 = ()

t1 = (1,2,3)
print(t1)
print(type(t1))

t2 = 1,3,4
print(t2)

t3 = t1,(5,6,7)
print(t3)

t4 = [1,4],[5,6]
print(t4)

t5 = tuple([1,4])
print(t5)

# 튜플의 요소 다루기
# 요소 변경 불가능
# print(t1[2])
# t1[2] = 10

# 요소 추가
# t1.append(-9)
# del[t1[2]]

# list1 = [1,2,3]
# del(list1[1])
# print(list1)
#
# del(t1)
# print(t1)

# tuple.index(), .count()

# tt = 'a','b','c','e','a','d'
# i = tt.index('e')
# print(i)
# c = tt.count('a')
# print(c)
#
# # slicing
# t = tt[:]
# t = tt[1:5]
# print(t)
#
# # +, * 연산
# print(t1 + t2)
# print(tt*2)

# tuple 연습문제  123 456 789 출력하기(소괄호 없이)
tt = ((1,2,3),(4,5,6),(7,8,9))
print(tt[1][2])

for i in tt:
    for a in i:
        print(a, end=' ')
    print()

# tuple
myTuple = (10,20,30)
a = (40,)
myTuple += a
print(myTuple)
# myTuple = (10,20,30,40)

print(t4[0])
print(type(t4[0]))
t4[0][0] = 10
print(t4)