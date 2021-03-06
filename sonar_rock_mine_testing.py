# -*- coding: utf-8 -*-
"""sonar_rock_mine_testing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q8qIf-i9UjotzFprGckJvLYTJTvDBLfX
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Copy of sonar data.csv', header = None)
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:, -1].values

print(x)

print(y)

from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(x,y , test_size = 0.2, random_state= 0)

print(train_x)

print(test_x)

from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression(random_state = 0)
regressor.fit(train_x,train_y)

y_pred = regressor.predict(test_x)
print(np.concatenate((y_pred.reshape(len(y_pred),1), test_y.reshape(len(test_y),1)),1))

from sklearn.metrics import confusion_matrix , accuracy_score
cm = confusion_matrix(test_y, y_pred)
print(cm)
print(accuracy_score(test_y, y_pred))

input_data = (0.0299,0.0688,0.0992,0.1021,0.0800,0.0629,0.0130,0.0813,0.1761,0.0998,0.0523,0.0904,0.2655,0.3099,0.3520,0.3892,0.3962,0.2449,0.2355,0.3045,0.3112,0.4698,0.5534,0.4532,0.4464,0.4670,0.4621,0.6988,0.7626,0.7025,0.7382,0.7446,0.7927,0.5227,0.3967,0.3042,0.1309,0.2408,0.1780,0.1598,0.5657,0.6443,0.4241,0.4567,0.5760,0.5293,0.3287,0.1283,0.0698,0.0334,0.0342,0.0459,0.0277,0.0172,0.0087,0.0046,0.0203,0.0130,0.0115,0.0015)
 # making an array changing the input_data to a numpy array
input_data_as_numpy_array = np.array(input_data)
 # reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = regressor.predict(input_data_reshaped)
print(prediction)
if prediction[0] == 'R':
  print("this is rock")
else:
  print("this is mine")

