# 리스트의 주요 메소드

# 리스트의 길이 계산 함수 : len(리스트명)
a = [1,2,3,4,5,6,3,9,3]
print(len(a))

# 리스트의 요소
print(a.count(3))

# 리스트의 요소 추가, 삽입 : append(), insert()
a.append(100)
print(a)

a.append([110, 120])
print(a)

a.insert(2, 120)
print(a)

b = []
print(b)
b.append(5.5)
print(b)
b.append(10.5)
print(b)
b.append(6.5)
print(b)

scores = []
for i in range(10):
    score = int(input('점수입력 :'))
    scores.append(score)
    scores.insert(0, score1)
print(scores)

# 리스트의 요소 제거 : remove(), pop()

# 리스트의 확장 : extend()

# 리스트의 요소를 정렬 : sort(), reverse()

# 리스트의 요소 찾기 : index()

# 리스트 요소 중 큰 값 (max()), 작은 값 (min())