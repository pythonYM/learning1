#https://tellusxdp.github.io/start-python-with-tellus/index.html
import pandas as pd
btc_price = pd.read_csv('coindesk-bpi-USD-close_data-2018-06-07_2018-06-27.csv')
btc_price.head()
print(btc_price.head())
""""""
X = btc_price.loc[0:499, ["Close Price"]]
y = btc_price.loc[1:500, ["Close Price"]]
print(X)
print(y)
""""""
import numpy as np
X_train = np.array(X[:400])
X_test  = np.array(X[400:])
y_train = np.array(y[:400])
y_test  = np.array(y[400:])

from sklearn import linear_model
model = linear_model.LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#print(y_pred)
#print(y_test)

import matplotlib.pyplot as plt
plt.plot(range(0,100), y_test, label='Actual price', color='blue')
plt.plot(range(0,100), y_pred, label='Predicted price', color='red')
plt.xlabel('Hours')
plt.ylabel('Price ($)')
plt.title('Bitcoin Price')
plt.grid(True)
plt.legend(loc = "upper left")
