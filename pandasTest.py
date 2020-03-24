import requests
import pandas as pd
import mplfinance as mpf

res = requests.get('https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc')
data = res.json()['result']['300']  # 15分足を使用する



col = ['time', 'Open', 'High', 'Low', 'Close', 'Volume', 'trade_value']
df = pd.DataFrame(data, columns=col)
df = df.set_index('time')  # time列をindexにする
df.index = pd.to_datetime(df.index, unit='s')  # unixtimeからdatetimeに変換する

mpf.plot(df, type='candle', volume=True, mav=(3,6,9), style='yahoo')



