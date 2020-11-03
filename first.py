
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
sns.set(font_scale= 2.5)

import missingno as msno

import warnings
warnings.filterwarnings('ignore')



# %matplotlib inline

# dataset 확인
train = pd.read_csv('D:/dataset/train.csv')
test = pd.read_csv('D:/dataset/test.csv')

print(train.describe())
print(test.describe())

# Null data check
for col in train.columns:
    msg = 'column: {:>10}\t Percent of NaN value: {:,.2f}%'.format(col, 100
* (train[col].isnull().sum() / train[col].shape[0]))
    print(msg)

for col in test.columns:
    msg = 'column: {:>10}\t Percent of NaN value: {:,.2f}%'.format(col, 100
* (test[col].isnull().sum() / test[col].shape[0]))
    print(msg)

# train, test 둘다 Age 19.87%, cabin 77.10%, embarked 0.22%

msno.matrix(df = train.iloc[:, :], figsize=(8,8), color=(0.8, 0.5, 0.2)) 

msno.bar(df = train.iloc[:, :], figsize=(8,8), color=(0.8, 0.5, 0.2)) 

msno.bar(df = test.iloc[:, :], figsize=(8,8), color=(0.8, 0.5, 0.2)) 

f, ax = plt.subplots(1, 2, figsize = (18, 8))

train['Survived'].value_counts().plot.pie

