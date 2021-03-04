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
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix

# データの保存
import pickle

from sklearn.preprocessing import MinMaxScaler
# モデルの学習
from sklearn.svm import SVC
from sklearn import svm 
# モデルの精度を評価する
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Hiragino Sans' # 日本語を含むフォントを指定
import numpy as np
from mlxtend.plotting import plot_decision_regions
from sklearn.linear_model import LogisticRegression

X = pd.read_csv('trainingData.csv',sep=",",header=0,usecols=[0,1,2])
y = pd.read_csv('trainingData.csv',sep=",",header=0,usecols=[4])

y = y.y # テストデータをDataframeに変換

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=None)

with open('X_train', 'rb') as f:
  X_train = pickle.load(f)
with open('X_test', 'rb') as f:
  X_test = pickle.load(f)
with open('y_train', 'rb') as f:
  y_train = pickle.load(f)
with open('y_test', 'rb') as f:
  y_test = pickle.load(f)

# データの正規化
mm = preprocessing.MinMaxScaler()
X_train_std = mm.fit_transform(X_train)
X_test_std = mm.fit_transform(X_test)

def param():
    ret = {
        'C' :[1,10,100],
        'gamma' : np.linspace(0.01, 1.0, 50)
    }
    return ret

# GridSearchCVのインスタンスを作成＆学習＆スコア記録
gscv = GridSearchCV(SVC(), param(), cv = 3, verbose=2)
gscv.fit(X_train_std, y_train)

# スコアの一覧を取得
gs_result = pd.DataFrame.from_dict(gscv.cv_results_)
gs_result.to_csv('gs_result.csv')

# 最高性能のモデルを取得し，テストデータを分類
best = gscv.best_estimator_ # bestを保存
pred = best.predict(X_test_std) # X_test_stdを保存

# # 混同行列を出力
print(confusion_matrix(y_test, pred))

# # テストデータに対する精度
accuracy_test = accuracy_score(y_test, pred) # y_testを保存
print('テストデータ（グリッドサーチ）に対する正解率： %.2f' % accuracy_test)

# # 線形SVMのインスタンスを生成
model = SVC(kernel='rbf', random_state=None)
 
# # モデルの学習．fit関数で行う．
model.fit(X_train_std, y_train)

# # トレーニングデータに対する精度
pred_train = model.predict(X_train_std)
accuracy_train = accuracy_score(y_train, pred_train)
print('トレーニングデータに対する正解率： %.2f' % accuracy_train)

# # テストデータに対する精度
pred_test = model.predict(X_test_std)
accuracy_test = accuracy_score(y_test, pred_test)
print('テストデータに対する正解率： %.2f' % accuracy_test)


# # 分類結果を図示する（三次元）
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

# 軸ラベルの設定
ax.set_xlabel("X\n時間的切迫感を与える単語")
ax.set_ylabel("Y\n頻出単語")
ax.set_zlabel("Z\n発話速度")

X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))

def getcolor(cl):
    if cl==0:
        return 'red' 
    elif cl==1:
        return 'blue' 
    else:
        return 'green'

colors = list(map(getcolor, y_combined))

ax.scatter(X_combined_std[:,0], X_combined_std[:,1], X_combined_std[:,2], color=colors)

plt.show()


# #CSV出力用
# print('%.2f, %.2f' % (accuracy_train, accuracy_test))

# # 分類結果を図示する（二次元）
# plt.style.use('ggplot') 

# X_combined_std = np.vstack((X_train_std, X_test_std))
# y_combined = np.hstack((y_train, y_test))

# # fig = plt.figure(figsize=(13,8))
# plot_decision_regions(X_combined_std, y_combined, clf=model,  res=0.02)
# plt.xlabel("X\n時間的切迫感を与える単語")
# plt.ylabel("Y\n頻出単語")
# plt.show()