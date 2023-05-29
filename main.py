import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt

from translations import HISTORY_FIELD_MAPPINGS

data_frame = pd.read_csv("S Mellat.Bank.csv")
data_frame = data_frame.iloc[::-1].reset_index(drop=True)
data_frame = data_frame.rename(columns=HISTORY_FIELD_MAPPINGS)
data_frame = data_frame.drop(columns=["<PER>", "<TICKER>"])
data_frame = data_frame.drop_duplicates(keep=False)
data_frame.date = pd.to_datetime(data_frame.date, format="%Y%m%d")
data_frame = data_frame.set_index(data_frame.date)
data_frame = data_frame.drop(columns=["date"])
print(data_frame)
adj_close = data_frame.adjClose.iloc[-50:]
print(adj_close)
max_idx = list(argrelextrema(adj_close.values, np.greater, order=3)[0])
min_idx = list(argrelextrema(adj_close.values, np.less, order=3)[0])

idx = max_idx + min_idx
idx.sort()
peaks = adj_close.values[idx]
plt.plot(adj_close.values)
plt.scatter(idx, peaks, c="r")
plt.show()
