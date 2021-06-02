import numpy as np

# 배열의 슬라이싱
b = np.array([0,10,20,30,40,50])
b1 = b[1:4]
print(b1)

print('-'*30)

b1 = b[:3]
print(b1)

print('-'*30)


b1 = b[2:]
print(b1)

print('-'*30)


# 원소 변경
b1 = b[2:5] = np.array([25,35,45])
print(b1)

print('-'*30)


b[3:6] = 60
print(b)

print('-'*30)

# 2차원 배열의 슬라이싱
b = np.arange(10,100,10).reshape(3,3)
print(b)

print('-'*30)

b2 = b[1:3,1:3]
print(b2)

print('-'*30)

# 일부 생략
b2 = b[:3,1:]
print(b2)

print('-'*30)

# 행 지정 열 슬라이싱
b2 = b[1][0:2]
print(b2)

print('-'*30)

# 슬라이싱 된 배열에 값 지정
b[0:2, 1:3] = np.array([[25,35],[55,65]])
print(b)