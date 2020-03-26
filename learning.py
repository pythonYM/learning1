import pandas as pd
import numpy as np
from pandas import DataFrame

wine_data_set = pd.read_csv("w.csv",sep=";",header=0)

#説明変数(ワインに含まれる成分)
X = DataFrame(wine_data_set.drop("quality",axis=1))

#目的変数(各ワインの品質を10段階評価したもの)
y = DataFrame(wine_data_set["quality"])

from sklearn.model_selection import train_test_split

X_train,X_test,y_learn,y_test=train_test_split(X,y,random_state=0)
print(X_train.shape)
print(X_test.shape)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(X_train, y_train)

model.score(X_test, y_test)

