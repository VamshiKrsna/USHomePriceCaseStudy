import os
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv

load_dotenv()
FRED_API_KEY = os.getenv("FRED_API_KEY")

fred = Fred(api_key=FRED_API_KEY)

data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

series_list = [
    'CPIAUCSL',  # Consumer Price Index for All Urban Consumers: Seasonally Adjusted (CPI-U)
    'CSUSHPISA',  # S&P Case-Shiller US National Home Price Index
    'FEDFUNDS',  # Effective Federal Funds Rate
    'GDB',  # Gross Domestic Product
    'HOUST',  # Housing Starts
    'MCOILWTICO',  # Crude Oil Prices (West Texas)
    'MEHOINUSA672N',  # Median Household Income
    'MORTGAGE15US',  # 15 Years Fixed rate mortgage average
    'MORTGAGE30US',  # 30 Years Fixed rate mortgage average
    'POP',  # Population in the US
    'UNRATE'  # Unemployment Rate
]

# I have included more explanation about above features in descriptions.txt

for series in series_list:
    data = fred.get_series(series)
    df = data.reset_index()
    df.columns = ['date', 'value'] 
    df.to_csv(os.path.join(data_dir, f'{series}.csv'), index=False)
    print(f'Saved {series} to {data_dir}/{series}.csv')
    print(df.head())  