# numpy 연산
import numpy as np
arr1 = np.array([10,20,30,40])
arr2 = np.array([1,2,3,4])

# 기본 연산
print(arr1 + arr2)

print(arr1 - arr2)

print(arr2 * 2)

print(arr2 ** 2)

print(arr1 * arr2)

print(arr1 / arr2)

# 크기를 비교해서 참 거짓으로 반환 가능
print(arr1 > 20)

# 통계를 위한 연산
arr3 = np.arange(5)
print(arr3)

# 배열의 합 , 평균
arr = [arr3.sum(), arr3.mean()]
print(arr)

# 배열의 표준편차, 분산
arr = [arr3.std(), arr3.var()]
print(arr)

# 배열의 최솟값, 최댓값
arr = [arr3.min(), arr3.max()]
print(arr)

# 배열의 누적 합, 누적 곱
arr4 = np.arange(1,5)
print(arr4)

arr = arr4.cumsum()
print(arr)

arr = arr4.cumprod()
print(arr)

# 행렬 연산
A = np.array([0,1,2,3]).reshape(2,2)
print(A)

B = np.array([3,2,0,1]).reshape(2,2)
print(B)

# 행렬 곱
a = A.dot(B)
print(a)
a = np.dot(A,B)
print(a)

# 전치 행렬
a = np.transpose(A)
print(a)
a = A.transpose()
print(a)

# 역행렬
a = np.linalg.inv(A)
print(a)

# 행렬식
a = np.linalg.det(A)
print(a)