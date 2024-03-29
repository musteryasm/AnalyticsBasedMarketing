# -*- coding: utf-8 -*-
"""Predictor_Marketing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lLj4OMiumQDCT0h8xYI9n8bL21iu5LtD

###Importing data
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression

dataset=pd.read_excel("/content/drive/MyDrive/MLminiproject/a2_Dataset_90Percent.xlsx")
# !ls

#shows first few rows of the code
dataset.head()

"""### Data preprocessing"""

# explore missing values
dataset.isna().sum()

# filling missing values with mean/mode*
dataset['DemAffl']=dataset['DemAffl'].fillna(dataset['DemAffl'].mode()[0])
dataset['DemAge']=dataset['DemAge'].fillna(dataset['DemAge'].mode()[0])
dataset['DemClusterGroup']=dataset['DemClusterGroup'].fillna(dataset['DemClusterGroup'].mode()[0])
dataset['DemGender']=dataset['DemGender'].fillna(dataset['DemGender'].mode()[0])
dataset['DemReg']=dataset['DemReg'].fillna(dataset['DemReg'].mode()[0])
dataset['DemTVReg']=dataset['DemTVReg'].fillna(dataset['DemTVReg'].mode()[0])
dataset['LoyalTime']=dataset['LoyalTime'].fillna(dataset['LoyalTime'].mean())

# explore missing values post missing value fix
dataset.isna().sum()

"""###Coverting category to numeric"""

# converting to mumeric
from sklearn.preprocessing import LabelEncoder
number = LabelEncoder()

dataset['DemClusterGroup'] = number.fit_transform(dataset['DemClusterGroup'].astype('str'))
integer_mapping = {l: i for i, l in enumerate(number.classes_)}
print(integer_mapping)

dataset['DemGender'] = number.fit_transform(dataset['DemGender'].astype('str'))
integer_mapping = {l: i for i, l in enumerate(number.classes_)}
print(integer_mapping)

dataset['DemReg'] = number.fit_transform(dataset['DemReg'].astype('str'))
integer_mapping = {l: i for i, l in enumerate(number.classes_)}
print(integer_mapping)

dataset['DemTVReg'] = number.fit_transform(dataset['DemTVReg'].astype('str'))
integer_mapping = {l: i for i, l in enumerate(number.classes_)}
print(integer_mapping)

dataset['LoyalClass'] = number.fit_transform(dataset['LoyalClass'].astype('str'))
integer_mapping = {l: i for i, l in enumerate(number.classes_)}
print(integer_mapping)

dataset.head()

"""### Predictions"""

X_fresh = dataset.iloc[:, 1:10].values

import joblib
classifier = joblib.load('/content/drive/MyDrive/MLminiproject/Copy of c2_Classifier_LoyalCustomers')

y_pred = classifier.predict(X_fresh)
print(y_pred)

predictions = classifier.predict_proba(X_fresh)
predictions

# writing model output file
df_prediction_prob = pd.DataFrame(predictions, columns = ['prob_0', 'prob_1'])
dfx=pd.concat([dataset,df_prediction_prob], axis=1)
dfx.to_excel("d2_BuyProb_90Percent.xlsx")
dfx.head()

