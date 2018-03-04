# -*- coding: utf-8 -*-
"""

@author: Ajay Gautam M

"""

#You do not talk about Fight Club
import os
os.chdir('....\\data\\input.csv')

#You DO NOT talk about Fight Club
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from fancyimpute import KNN
from sklearn import svm

#Only two guys to a fight
train = pd.read_csv('train.csv')
test  = pd.read_csv('test.csv')

#Someone yells stop, goes limp, taps out, the fight is over
train.isnull().sum()
train = KNN(k=3).complete(train)
test  = KNN(k=3).complete(test)

#One fight at a time
le = LabelEncoder()
cat = ['genre','certificate', 'distributor']
for col in cat:
    train[col] = le.fit_transform(train[col])
    test[col] = le.fit_transform(test[col])

#no shirts, no shoes
train_X = train.drop(['year','oscar', 'movie_name', 'actor_name', 'href'], axis=1)  
test_X = test.drop(['year','oscar', 'movie_name', 'actor_name', 'href'], axis = 1)
 
train_Y = train['oscar']

#Fights will go on as long as they want to
svm =svm.SVC(kernel='rbf',C=1).fit(train_X,train_Y)
svm.score(train_X, train_Y)

#If this is your first night at Fight Club, you have to fight.
pred_svm = svm.predict_proba(test_X)[:,1]
svm_prediction = pd.DataFrame(pred_svm, test['movie_name'])

















