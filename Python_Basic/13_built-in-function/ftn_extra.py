# 재귀함수

# def selfCall():
#     print('ha', end='')
#     selfCall()
#
# selfCall()

# 팩토리얼 계산
def fact(num):
    if num == 1 :
        return 1
    else:
        return num*fact(num-1)
print(fact(5))

# 자연수를 입력받으면 해당하는 자연수까지 출력하는 재귀함수
# 49 입력하면 49~1으로 출력
def count(num):
    a = []
    for i in range(num,0,-1):
        a.append(i)
        # print(max(a),min(a))
    return a
print(max(count(49)),'~',min(count(49)))

def hap(x=10,y=20):
    return x+y

print(hap())
print(hap(30,100))

hap3 = lambda x =10, y = 20 : x+y
print(hap3())
print(hap3(9,10))

# 람다함수 안에서 변수를 생성할 수 없다
# print((lambda x: y=10, x+y)(10))

y = 10
print((lambda x: x+y)(1))

# 람다함수 list 사용
# 리스트의 값에 각각 10을 더하는 람다함수를 작성

# 10을 더하는 함수
def addTen(x):
    return x + 10

print(list(map(addTen, [1,3,4])))

map(lambda x:x+10, [1,3,4])
print(list(map(lambda x:x+10, [1,3,4])))

# 두개의 리스트의 같은 요소의 값들을 더해서 하나의 리스트로 반환
# 1) def 함수 정의
# 2) lambda 표현식 정의

def addList(x,y):
    addlist = []
    add = list(zip(x,y))
    for i in add:
        i = (i[0]+i[1])
        addlist.append(i)
    return addlist

list1 = [1,2,3,4]
list2 = [10,20,30,40]
result = addList(list1,list2)
print(result)

print(list(map(lambda x,y:x+y,list1,list2)))