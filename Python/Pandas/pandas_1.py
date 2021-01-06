import numpy as np
import pandas as pd

# Series
# - pandas의 기본 객체 중 하나
# - numpy의 ndarray를 기반으로 인덱싱 기능을 추가하여 1차원 배열을 나타냄
# - index를 지정하지 않을 시, 기본적으로 ndarray와 같이 0-based 인덱스 생성,
#   지정할 경우 명시적으로 지정된 index를 사용
# - 같은 타입의 0개 이상의 데이터를 가질 수 있음

# - data로만 생성하기
# -- index는 기본적으로 0부터 자동적으로 생성

s1 = pd.Series([1,2,3])
# print(s1)

# 0    1
# 1    2
# 2    3
# dtype: int64

s2 = pd.Series(['a','b','c'])
# print(s2)

# 0    a
# 1    b
# 2    c
# dtype: object

s3 = pd.Series(np.arange(200))
# print(s3)

# 0        0
# 1        1
# 2        2
# 3        3
# 4        4
#       ...
# 195    195
# 196    196
# 197    197
# 198    198
# 199    199
# Length: 200, dtype: int32

# - data, index 함께 명시하기

s4 = pd.Series([1,2,3], [100,200,300])
# print(s4)

# 100    1
# 200    2
# 300    3
# dtype: int64

s5 = pd.Series([1,2,3],['a','m','k'])
# print(s5)

# a    1
# m    2
# k    3
# dtype: int64

# - data, index, data type 함께 명시하기

s6 = pd.Series(np.arange(5), np.arange(100, 105), dtype=np.int16)
# print(s6)

# 100    0
# 101    1
# 102    2
# 103    3
# 104    4
# dtype: int16

# 인덱스 활용하기

s6.index
# Int64Index([100, 101, 102, 103, 104], dtype='int64')

s6.values
# [0 1 2 3 4]

# 1. 인덱스를 통한 데아터 접근

s6[104]
# 4

# s6[105]
# 오류 발생 > 105 인덱스가 없음

# 2. 인덱스를 통한 데이터 업데이트

s6[104] = 70
# print(s6)

# 100     0
# 101     1
# 102     2
# 103     3
# 104    70
# dtype: int16

s6[105] = 90
s6[200] = 80

# print(s6)

# 100     0
# 101     1
# 102     2
# 103     3
# 104    70
# 105    90
# 200    80
# dtype: int64

# 3. 인덱스 재사용하기
s7 = pd.Series(np.arange(7), s6.index)
# print(s7)

# 100    0
# 101    1
# 102    2
# 103    3
# 104    4
# 105    5
# 200    6
# dtype: int32

