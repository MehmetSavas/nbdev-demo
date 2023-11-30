# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_data_handler.ipynb.

# %% auto 0
__all__ = ['some_api_call', 'transform_data', 'convert_to_float']

# %% ../nbs/00_data_handler.ipynb 3
def some_api_call():
    """This function replicates an API call that returns a list of data."""
    return [45, 37, 35, 30, 31, 28, 27, 33, 35, 34, 52, 56,
             67, 80, 82, 81, 76, 96, 100, 101, 78, 52, 48, 46]

# %% ../nbs/00_data_handler.ipynb 10
import pandas as pd

# %% ../nbs/00_data_handler.ipynb 11
def transform_data(data: list # List of hourly prices
                  ):
    """Transforms data into dataframe with hours defined."""
    hours = [x for x in range(0, 24, 1)]
    df = pd.DataFrame({'time': hours, 'price': data})
    return df

# %% ../nbs/00_data_handler.ipynb 12
def convert_to_float(data: pd.DataFrame # Hourly prices dataframe
                    ):
    """Converts price column to float type."""
    data['price'] = data['price'].astype(float)
    return data