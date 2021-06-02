import numpy as np

a = np.array([0,10,20,30,40,50])
print(a)

print('-'*30)

# 배열 위치 지정
a1 = a[0]
print(a1)

print('-'*30)

# 배열의 원소 변경
a1 = a[5] = 70
print(a)

print('-'*30)

# 1차원 배열에서 여러 개의 원소 선택
a1 = a[[1,3,4]]
print(a1)

print('-'*30)

# 2차원 배열에서 원소 선택
a1 = np.arange(10,100,10).reshape(3,3)
print(a1)

print('-'*30)

a2 = a1[0,2] # 행 위치 0, 열 위치 2
print(a2)

print('-'*30)

# 원소 값 변경
a2 = a1[2,2] = 95
print(a1)

print('-'*30)

# 행 전체 가져오기
a2 = a1[1]
print(a2)

print('-'*30)

# 특정 행 지정해 전체 값 바꾸기
a2 = a1[1] = np.array([45,55,65])
print(a1)

print('-'*30)

# 2차원 배열의 여러 원소 선택하기
a2 = a1[[0,2],[0,1]]
print(a2)

print('-'*30)

# 배열에 조건 지정
a1 = np.array([1,2,3,4,5,6])
print(a1[a1 > 3])

print('-'*30)

print(a1[(a1 % 2) == 0])

