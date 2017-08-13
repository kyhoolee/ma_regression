import pandas as pd


def read_ma():
    ma_data = pd.read_csv("../data/mba_csv.csv")
    ma_data.head()

    ma_array = ma_data.values
    rows, cols = ma_array.shape
    print rows, cols
    ma_target = ma_array[:, 0]
    ma_x = ma_array[:, 1:cols]

    print ma_target.shape
    print ma_x.shape

    return (ma_x, ma_target)