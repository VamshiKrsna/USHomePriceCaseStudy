import numpy as np
import pandas as pd
import missingno as mno

# Please Refer descriptions.txt to understand the involved features.

data_dir = "../data"

# Loading csv files : 
cpi = pd.read_csv('..//data//CPIAUCSL.csv')
csus = pd.read_csv('..//data//CSUSHPISA.csv')
fedfunds = pd.read_csv('..//data//FEDFUNDS.csv')
gdp = pd.read_csv('..//data//GDB.csv')
houst = pd.read_csv('..//data//HOUST.csv')
mcoil = pd.read_csv('..//data//MCOILWTICO.csv')
meho = pd.read_csv('..//data//MEHOINUSQ672N.csv')
mort15 = pd.read_csv('..//data//MORTGAGE15US.csv')
mort30 = pd.read_csv('..//data//MORTGAGE30US.csv')

print(cpi.head())