import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
print('Setup complete')

# Load and display train data
train_data = pd.read_csv("D:\\dataset\\titanic\\train.csv")
print(train_data.head())

# Load and display test data
test_data = pd.read_csv("D:\\dataset\\titanic\\test.csv")
print(test_data.head())

print(train_data.info())
print(test_data.info())

Sur = train_data['Survived'].value_counts(normalize=True)
print(Sur)

g = sns.countplot(y = train_data['Survived']).set_title('Survivors and dead count')
plt.show()
