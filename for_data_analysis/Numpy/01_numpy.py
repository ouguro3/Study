# Numpy : 파이썬으로 과학 연산을 쉽고 빠르게 할 수 있게 만든 패키지
# 파이썬의 기본 데이터 형식과 내장 함수를 이용하는 것보다 다차원 배열 데이터를 효과적으로 처리

import numpy as np

# 1차원 배열 생성
data1 = [0,1,2,3,4,5]
a1 = np.array(data1)
print(a1)

# 실수와 정수 혼합된 리스트
data2 = [0.1,5,4,12,0.5]
a2 = np.array(data2)
print(a2)  # 실수와 정수가 혼합되어 있을 경우 모두 실수로 변환

# 타입 확인
print(a1.dtype) # int32
print(a2.dtype) # float64

# 2차원 배열 생성
data3 = ([[1,2,3],[4,5,6],[7,8,9]])
a3 = np.array(data3)
print(a3)

# 범위 지정해 배열 생성
aran1 = np.arange(0,10,2)
print(aran1)
aran2 = np.arange(1,10)
print(aran2)

# 1차원 배열 >> 2차원으로 변경
aran3 = np.arange(12).reshape(4,3) # 4행 3열
print(aran3)

# 배열의 형태
shp1 = aran3.shape
print(shp1)
shp2 = a1.shape
print(shp2)
# 다차원은 (m,n)의 형태로 1차원은 (m,)의 형태로 출력

# linspace() : 범위의 시작과 끝을 지정하고 데이터의 개수를 지정해 Numpy() 배열을 생성
lin1 = np.linspace(1,10,10) # 1부터 10까지 10개의 데이터 생성
print(lin1)

# 특별한 형태의 배열 ---

# zeros() : 0만으로 이루어진 배열
z = np.zeros(10)
print(z)

# zeros()를 이용해 2차원 배열 생성
z2 = np.zeros((3,4))
print(z2)

# ones() : 1만으로 이루어진 배열
o = np.ones(5)
print(o)

# ones() 2차원 배열
o2 = np.ones((3,5))
print(o2)
# ---

# 단위행렬 : 주 대각선이 모두 1이고 나머지는 0인 행렬
eye = np.eye(3)
print(eye)

# 배열의 데이터 타입 변환 astype()
str_a = np.array(['1','2','3','4','5'])
num_a = str_a.astype(int)
print(num_a)
print(str_a.dtype) # <U1 numpy 데이터의 형식이 유니코드이며, 문자의 수는 최대 1개
print(num_a.dtype)

# 난수 배열 생성
# rand() : 0과 1 사이의 난수 생성
ran1 = np.random.rand(2,3)
print(ran1)

# randint() : 지정한 범위에 해당하는 정수로 난수 배열을 생성
ran2 = np.random.randint(10, size=(3,4))
print(ran2)