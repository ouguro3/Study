# set

# 집합 만들기
# s1 = set()
# print(type(s1))
# s1 = {3,5,7,1,3,4}
# print(s1)

# s2 = {[10, 20, 40]}
# s2 = {(10,20,40)}
# print(s2)

# 인덱스 사용 불가
# s1[0]

# 데이터 추가 .add()
# s2.add(90)
# print(s2)

# s1.add(-9)
# print(s1)

# 데이터 삭제 .remove()
# s1.remove(-9)
# print(s1)
# s1.remove(8) # 값이 에러 발생
# print(s1)

# s1.discard(7)
# s1.discard(4)
# print(s1)
#
# s1.clear()
# print(s1)

# del s1
# print(s1)

# 집합 연산 : union, intersection, difference

s1 = {3,4,1,6}
s2 = {2,4,5,8,3}
print(s1.union(s2)) # s1, s2 합
print(s1.intersection(s2))  # s1 , s2 의 동일한값
print(s1.difference(s2)) # s2에 없는 s1의 값

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)

# 컴프리헨션
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)