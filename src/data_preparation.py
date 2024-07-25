import numpy as np
import pandas as pd
import os

cwd = os.getcwd()

data_dir = os.path.join(cwd, 'data')

cpi = pd.read_csv(os.path.join(data_dir, 'CPIAUCSL.csv'))
csus = pd.read_csv(os.path.join(data_dir, 'CSUSHPISA.csv'))
fedfunds = pd.read_csv(os.path.join(data_dir, 'FEDFUNDS.csv'))
gdp = pd.read_csv(os.path.join(data_dir, 'GDB.csv'))
houst = pd.read_csv(os.path.join(data_dir, 'HOUST.csv'))
mcoil = pd.read_csv(os.path.join(data_dir, 'MCOILWTICO.csv'))
meho = pd.read_csv(os.path.join(data_dir, 'MEHOINUSA672N.csv'))
mort15 = pd.read_csv(os.path.join(data_dir, 'MORTGAGE15US.csv'))
mort30 = pd.read_csv(os.path.join(data_dir, 'MORTGAGE30US.csv'))

print(cpi.head())

