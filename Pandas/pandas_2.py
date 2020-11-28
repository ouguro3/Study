import numpy as np
import pandas as pd

# Series size, shape, unique, count, value_counts 함수
# - size : 개수 반환
# - shape : 튜플 형태로 shape 반환
# - unique: 유일한 값만 ndarray로 반환
# - count: NaN을 제외한 개수를 반환
# - mean: NaN을 제외한 평균
# - value_counts: NaN을 제외하고 각 값들의 빈도를 반환

s = pd.Series([1,1,2,1,2,2,2,1,1,3,3,4,5,5,7,np.NaN])
# print(s)

# 0     1.0
# 1     1.0
# 2     2.0
# 3     1.0
# 4     2.0
# 5     2.0
# 6     2.0
# 7     1.0
# 8     1.0
# 9     3.0
# 10    3.0
# 11    4.0
# 12    5.0
# 13    5.0
# 14    7.0
# 15    NaN
# dtype: float64

len(s)
# 16
s.size
# 16
s.shape
# (16,)
s.unique()
# [ 1.  2.  3.  4.  5.  7. nan]
s.count()
# 15

a = np.array([2,2,2,2, np.NaN])
a.mean
# <built-in method mean of numpy.ndarray object at 0x0000018389F1B940>

b = pd.Series(a)
b.mean

# <bound method Series.mean of 0    2.0
# 1    2.0
# 2    2.0
# 3    2.0
# 4    NaN
# dtype: float64>

s.mean

# <bound method Series.mean of 0     1.0
# 1     1.0
# 2     2.0
# 3     1.0
# 4     2.0
# 5     2.0
# 6     2.0
# 7     1.0
# 8     1.0
# 9     3.0
# 10    3.0
# 11    4.0
# 12    5.0
# 13    5.0
# 14    7.0
# 15    NaN
# dtype: float64>

s.value_counts()

# 1.0    5
# 2.0    4
# 5.0    2
# 3.0    2
# 7.0    1
# 4.0    1
# dtype: int64


