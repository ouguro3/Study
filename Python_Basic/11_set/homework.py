# 실습문제 : Tuple & Set

# 1. my_variable 이름의 비어있는 튜플을 만들라.
print('1. my_variable = ()')
my_variable = ()
print(my_variable)

# 2. 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#  File "<pyshell#46>", line 1, in <module>
#  t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

print('2. 튜플의 요소값은 변경할 수 없다')


# 3. 숫자 1 이 저장된 튜플을 생성하라.

print('3. a = (1,)')
a = (1,)
print(a)

# 4. 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4

print('4. 튜플은 괄호와 함께 정의해야하는데 편의상 생략이 가능하다')

# 5. 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
#  t = ('a', 'b', 'c')

print('5. 튜플의 값은 변경이 불가능하므로 그냥 새로운 t를 정의해서 거기에 업데이트 한다')
t = ('A','b','c')

# 6. 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')

print('6.',end='\t')
interest = ('삼성전자', 'LG전자', 'SK Hynix')
lis = list(interest)
print(lis)

# 7. 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']

print('7.',end='\t')
interest = ['삼성전자', 'LG전자', 'SK Hynix']
tup = tuple(interest)
print(tup)

# 8. 파티에 참석한 사람이 다음과 같을 때 집합을 생성하고, 아래 조건에 맞게 출력하시오.
# partyA : "Park","Kim","Lee"
# partyB : "Park","길동","몽룡"

# 1) 파티에 참석한 모든 사람은?
# 2) 2개의 파티에 모두 참석한 사람은?
# 3) 파티 A에만 참석한 사람
# 4) 파티 B에만 참석한 사람

partyA = {"Park","Kim","Lee"}
partyB = {"Park","길동","몽룡"}

print('8_1',end='\t')
a = (partyA.union(partyB))
print(a)
print('8_2',end='\t')
a = (partyA.intersection(partyB))
print(a)
print('8_3',end='\t')
a = (partyA.difference(partyB))
print(a)
print('8_4',end='\t')
a = (partyB.difference(partyA))
print(a)
