import pandas as pd
import numpy as np

df_train = pd.read_csv("C:/Users/191016PM/Downloads/winequality-red.csv")

df_train.density.value_counts()

X=df_train.loc[:, ["density"]]
y=df_train.loc[:, "quality"]

from sklearn.model_selection import train_test_split

X_train,X_test,y_learn,y_test=train_test_split(X,y,random_state=0)
print(X_train.shape)
print(X_test.shape)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(X_train, y_train)

model.score(X_test, y_test)

