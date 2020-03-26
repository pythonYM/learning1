from idlelib.idle_test.test_browser import f1

import pandas as pd
from scipy.constants import precision
from sklearn.model_selection import train_test_split


df = pd.read_csv("/Users/191016PM/Desktop/winequality.csv", sep=";", encoding="utf-8")
print(df)

wine_data_set = pd.read_csv("w.csv",sep=";",header=0)


# データをラベルとデータに分離
#dropメソッドでqualityラベルの付いた列を消す
#列に沿った処理はaxis=0
#行に沿った処理はaxis=1
y = df["quality"]
x = df.drop("quality", axis=1)


# データを学習用とテスト用に分割する
#train_test_split には以下のような引数を与えます。
#第一引数: 特徴行列 X
#第二引数: 目的変数 y

#X_train: トレーニング用の特徴行列（「アルコール度数」「密度」「クエン酸」などのデータ）
#X_test: テスト用の特徴行列
#y_train: トレーニング用の目的変数（「美味しいワイン」か「そうでもないワインか」）
#y_test: テスト用の目的変数
#test_size=: テスト用のデータを何割の大きさにするか
#test_size=0.3 で、3割をテスト用のデータとして置いておく
(x_train, x_test, y_train, y_test) = train_test_split(x, y, test_size=0.3)

# データを学習
# ランダムフォレストで学習する
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train, y_train)

# 予測して精度を確認する
# 評価する
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score
from sklearn.metrics import accuracy_score


#predict(x, batch_size=None, verbose=0, steps=None)
#入力サンプルに対する予測の出力を生成します．

#引数について
#x: Numpy配列の入力データ（もしくはモデルが複数の出力を持つ場合はNumpy配列のリスト）．
#batch_size: 整数値．指定しなければデフォルトで32になります．
#verbose: 進行状況の表示モードで，0または1．
#steps: 予測ラウンド終了を宣言するまでの総ステップ数（サンプルのバッチ）．デフォルト値のNoneならば無視されます．
#戻り値:予測結果のNumpy配列．
y_pred = model.predict(x_test)


#classification_report
#分類問題の評価基準であるprecision(適合率)、recall(再現率)、f1-score(F値)、support(実際のサンプル数)を出力

#                precision    recall  f1-score   support

#           3       0.00      0.00      0.00         3
#           4       0.00      0.00      0.00        17
#           5       0.74      0.81      0.78       217
#           6       0.69      0.67      0.68       196
#           7       0.55      0.63      0.59        43
#           8       0.50      0.25      0.33         4

#    accuracy                           0.70       480
#   macro avg       0.41      0.39      0.40       480
#weighted avg       0.67      0.70      0.68       480

print(classification_report(y_test, y_pred))


#正解率 (Accuracy)
#正解率 (Accuracy) とは、「本来ポジティブに分類すべきアイテムをポジティブに分類し、
#本来ネガティブに分類すべきアイテムをネガティブに分類できた割合」を示し、以下の式で表されます。

#Accuracy = (TP + TN) / (TP + TN + FP + FN)

print("正解率 = ", accuracy_score(y_test, y_pred))





