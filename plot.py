import matplotlib.pyplot as plt
import requests

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

x = jsonData["quotes"][0]["high"]
y = x*x
plt.plot(x,y)
plt.show()