import matplotlib.pyplot as plt
import requests
import numpy as np

#とりあえず例として、どこかのWeb APIを叩くことにする
url = "http://www.gaitameonline.com/rateaj/getrate"

#requests.getを使うと、レスポンス内容を取得できるのでとりあえず変数へ保存
response = requests.get(url)

#response.json()でJSONデータに変換して変数へ保存
jsonData = response.json()

#このJSONオブジェクトは、連想配列（Dict）っぽい感じのようなので
#JSONでの名前を指定することで情報がとってこれる
print(jsonData["quotes"])
print(jsonData["quotes"][0])
print(jsonData["quotes"][0]["high"])

#responseから取得したJSONデータが単一のJSONオブジェクトではなく
#配列みたいになっているときはfor文と組み合わせてやるとよし。




# 描画範囲の指定
# x = np.arange(x軸の最小値, x軸の最大値, 刻み)

a=float(jsonData["quotes"][0]["high"])
b=float(jsonData["quotes"][0]["low"])



x = np.linspace(0,24,25)
y = np.linspace(b,a,25)
plt.plot(x,y)
plt.show()