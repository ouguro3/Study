import numpy as np

# 배열의 슬라이싱
b = np.array([10,20,30,40,50])
b1 = b[1:4]
print(b1)

b1 = b[:3]
print(b1)

b1 = b[2:]
print(b1)

# 원소 변경
b1 = b[2:5] = np.array([25,35,45])
print(b1)