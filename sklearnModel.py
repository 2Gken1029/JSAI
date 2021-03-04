#!python3
# -*- coding: utf-8 -*-
#matplotlib inline

# CSVデータの利用
import pandas as pd
from pandas import Series,DataFrame
from sklearn import preprocessing
# データの前処理
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
# データの保存
import pickle
from sklearn.preprocessing import MinMaxScaler
# モデルの学習
from sklearn.svm import SVC
# モデルの精度を評価する
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

X = pd.read_csv('trainingData.csv',sep=",",header=0,usecols=[0,1,2])
y = pd.read_csv('trainingData.csv',sep=",",header=0,usecols=[4])

y = y.y # テストデータをDataframeに変換

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=None)

with open('X_train', 'rb') as f:
  X_train = pickle.load(f)
with open('X_test', 'rb') as f:
  X_test = pickle.load(f)
with open('y_train', 'rb') as f:
  y_train = pickle.load(f)
with open('y_test', 'rb') as f:
  y_test = pickle.load(f)

# print(X_train)
# print(y_train)
# print(X_test)
# print(y_test)

# データの正規化
mm = preprocessing.MinMaxScaler()
X_train_std = mm.fit_transform(X_train)
X_test_std = mm.fit_transform(X_test)

# # 線形SVMのインスタンスを生成
model = SVC(kernel='rbf', random_state=None)
 
# # モデルの学習．fit関数で行う．
model.fit(X_train_std, y_train)

# # トレーニングデータに対する精度
pred_train = model.predict(X_train_std)
accuracy_train = accuracy_score(y_train, pred_train)
print(y_train)
# 混同行列を出力
print(confusion_matrix(y_train, pred_train))
print('トレーニングデータに対する正解率： %.3f' % accuracy_train)

# # テストデータに対する精度
pred_test = model.predict(X_test_std)
accuracy_test = accuracy_score(y_test, pred_test)
print(y_test)
# 混同行列を出力
print(confusion_matrix(y_test, pred_test))
print('テストデータに対する正解率： %.3f' % accuracy_test)