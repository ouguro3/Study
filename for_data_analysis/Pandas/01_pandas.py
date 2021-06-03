import numpy as np
import pandas as pd

# pandas Series
s1 = pd.Series([10,20,30,40,50])
print(s1)

print('-'*30)

print(s1.index)

print('-'*30)

print(s1.values)

print('-'*30)

# pandas는 데이터 타입이 달라도 OK
s2 = pd.Series(['a','b','c',1,2,3])
print(s2)

print('-'*30)

import numpy as np

# NaN 넣기
s3 = pd.Series([np.nan,10,30])
print(s3)

print('-'*30)

# Series 데이터를 생성할 때 인자로 index를 추가 가능하다
# s = pd.Series(seq_data, index = index_seq)
# 단 seq_data의 항목 개수와 index_seq 항목의 개수는 같아야 한다

index_date = ['2018-10-07','2018-10-08','2018-10-09','2018-10-10']
s4 = pd.Series([200,195,np.nan,205], index=index_date)
print(s4)

print('-'*30)

# 딕셔너리를 이용하면 data와 index를 함께 입력 가능
# s = pd.Series(dict_data)
s5 = pd.Series({'국어':100,'영어':95,'수학':90})
print(s5)

print('-'*30)

# 날짜 자동 생성 : date_range
date = pd.date_range(start='2019-01-01', end='2019-01-07')
print(date)

# 어떤 형식으로 입력하던지 날짜의 표기 형식은 yyyy-mm-dd 형식으로 바뀌어 출력된다
print('-'*30)



