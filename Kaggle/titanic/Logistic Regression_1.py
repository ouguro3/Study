import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
train_data = pd.read_csv('D:\\dataset\\titanic\\train.csv')
test_data = pd.read_csv('D:\\dataset\\titanic\\test.csv')

def sigmoid(z):
    return 1. / (1. + np.exp(-1 * z))

def featureNormalize(X):
    return np.divide((X - np.mean(X, axis=0)), np.std(X, axis=0, ddof=1))

def appendIntercept(X):
    N = np.shape(X)
    zeros = np.ones((N[0], N[1] + 1))
    zeros[:,1:] = X
    X = zeros
    return X

def logisticCostFunction(theta, X, y, lambd):
    m = len(y)
    h = sigmoid(np.matmul(X, theta))
    J = (1/m) * np.sum(np.multiply((-1 * y), np.log(h)) - np.multiply((1-y),np.log(1 - h)))
    J = J + (lambd / (2*m)) * np.sum(np.matmul(np.transpose(theta[1:]), theta[1:]))
    grad = (1/m) * np.matmul(np.transpose(X), h - y)
    grad[1:] = grad[1:] + (lambd/m) * theta[1:]
    return J, grad
def gradientDescent(X, y, theta, lambd, alpha, num_iters, cost_fuction):
    J_hist = list()
    for i in range(num_iters):
        J, grad = cost_fuction(theta, X, y, lambd)
        theta -= alpha * grad
        J_hist.append(J)
    return theta, J_hist
def linearCostFunction(theta, X, y):
    m = len(y)
    J = 0
    grad = np.zeros(len(theta))
    h = np.matmul(X, theta)
    J = (1/(2 * m)) * np.sum(np.power((h - y), 2))
    for i in range(len(theta)):
        grad[i] = (1/m) * np.sum(np.multiply((h - y), X[:,i]))
    return J, grad
def normalEquation(X,y):
    theta = 0
    theta = np.matmul(np.linalg.pinv(np.matmul(np.transpose(X), X)), np.matmul(np.transpose(X), y))
    return theta

X = np.matrix([[10,99,39], [10,30,40], [11,15,16]])

# Checking dataset for dirty records

# PassengerId - CLEAN
bad = len(train_data[train_data['PassengerId'] == 0])
print("PassengerIds set to 0: {}".format(bad))
bad = train_data["PassengerId"].isnull().sum()
print("Null Survived: {}".format(bad))

# Survived - CLEAN
bad = train_data["Survived"].isnull().sum()
print("Null Survived: {}".format(bad))

# Pclass - CLEAN
unique = train_data["Pclass"].unique()
print('Unique Pclass: {}'.format(unique))
bad = train_data["Pclass"].isnull().sum()
print("Null Pclass: {}".format(bad))

# Name - CLEAN
bad = train_data["Name"].isnull().sum()
print("Null Name: {}".format(bad))

# Sex -CLEAN
unique = train_data["Sex"].unique()
print("Unique Sex: {}".format(unique))
bad = train_data["Sex"].isnull().sum()
print("Null Sex: {}".format(bad))

# Age = 177 Dirty
maximum = train_data["Age"].max()
print("Maximum Age: {}".format(maximum))
bad = train_data["Age"].isnull().sum()
print("Null Age: {}".format(bad))

# SibSp - CLEAN
maximum - train_data["SibSp"].max()
print("Max SibSp: {}".format(maximum))
bad = train_data["SibSp"].isnull().sum()
print("Null SibSp: {}".format(bad))

# Parch - CLEAN
maximum = train_data["Parch"].max()
print('Max Parch: {}'.format(maximum))
bad = train_data["Parch"].isnull().sum()
print("Null Parch: {}".format(bad))

# Ticket Number - CLEAN
bad = train_data["Ticket"].isnull().sum()
print("Null Ticket: {}".format(bad))

# Fare - CLEAN
maximum = train_data["Fare"].max()
print("Max Fare: {}".format(maximum))
minimum = train_data["Fare"].min()
print("Min Fare: {}".format(minimum))
bad = train_data["SibSp"].isnull().sum()
print("Null Fare: {}".format(bad))

# Cabin - DIRTY, 687 BAD records
unique = train_data["Cabin"].unique()
print("Unique Cabin: {}".format(unique))
bad = train_data["Cabin"].isnull().sum()
print("Null Cabin: {}".format(bad))

# Embarked - DIRTY, 2 records
unique = train_data["Embarked"].unique()
print("Unique Embarked: {}".format(unique))
bad = train_data["Embarked"].isnull().sum()
print("Null Embarked: {}".format(bad))

# Break the data down into a train set, a cross validation set, and a test set

train_data_size = len(train_data.index)
train_set_size = int(train_data_size * .6)
cv_set_size = int(train_data_size * .2)
test_set_size = train_data_size - train_set_size - cv_set_size

print("Train set size: {}, CV set size: {}, Test set size: {}".format(train_set_size, cv_set_size,test_set_size))

train_set = train_data[:train_set_size]
cv_set = train_data[train_set_size:train_set_size + cv_set_size]
test_set = train_data[train_set_size + cv_set_size:train_set_size + cv_set_size + test_set_size]

assert len(train_set.index) == train_set_size
assert len(cv_set.index) == cv_set_size
assert len(test_set.index) == test_set_size

assert train_set["PassengerId"].max() != cv_set["PassengerId"].min()
assert cv_set["PassengerId"].max() != train_set["PassengerId"].min()

# Divide training dataset into a feature matrix and target vector
pd.options.mode.chained_assignment = None

y = train_set["Survived"]
X = train_set[["Pclass", "Sex"]]
X.Sex = pd.Categorical(X.Sex)
X["Sex"] = X.Sex.cat.codes
y = np.matrix(y.to_numpy()).T
X = X.to_numpy()
X_norm = featureNormalize(X)
X_norm = appendIntercept(X_norm)
X_norm_shape = np.shape(X_norm)
theta = np.zeros((X_norm_shape[1], 1))

theta, J_hist = gradientDescent(X_norm, y, theta, 0, 0.01, 10, logisticCostFunction)
print(J_hist)