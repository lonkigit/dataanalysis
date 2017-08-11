import pandas as pd
import datetime
import pandas_datareader as pdr

import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2015,8,22)

df = pdr.DataReader("XOM","yahoo",start,end)
# print(df)
print(df.head())

style.use('fivethirtyeight')

df['Low'].plot()
plt.legend()
plt.show()
