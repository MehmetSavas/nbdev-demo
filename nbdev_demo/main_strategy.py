# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_main_strategy.ipynb.

# %% auto 0
__all__ = ['predict_prices']

# %% ../nbs/01_main_strategy.ipynb 4
import pandas as pd
import numpy as np

# %% ../nbs/01_main_strategy.ipynb 11
def predict_prices(df: pd.DataFrame # Dataframe contains hourly prices
                  ):
    """Predict half hourly prices based on hourly prices."""
    hhp = []
    for ind, row in df.iterrows():
        if ind != len(df) - 1:
            hhp.append(row['price'])
            hhp.append((row['price'] + df.loc[ind+1, 'price']) / 2 * 0.98)
        else:
            hhp.append(row['price'])
            hhp.append(row['price'])
    return pd.DataFrame({'time': np.linspace(0, 24, 49)[0:-1],
                         'prices': hhp})