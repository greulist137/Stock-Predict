import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import requests

# Load in the stock symbol data.
stock_symbols = pd.read_csv("companylist.csv")

#Taking a quick peek at the un-edited dataset
print(stock_symbols.head())

#Only interested in the list of Symbols.  All other columns have been dropped
stock_symbols = stock_symbols.drop(['Name', 'LastSale', 'MarketCap', 'ADR TSO', 'IPOyear', 'Sector', 'Industry', 'Summary Quote', 'Unnamed: 9'], axis=1)

#Printing to get ensure only the Symbol column remains.  
print(stock_symbols.head())


#Checking shape of dataset to see how many Symbols are contained in the dataset
print(stock_symbols.shape)

#CREATE A FUNCTION THAT WILL CALL THE API WITH EACH CODE. 
cols = ['timestamp, open, high, low, close, volume']
df = pd.DataFrame(columns = cols)
for index, row in stock_symbols.iterrows():
    data = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=RVXYVXKGEGNOH2F7&datatype=csv'.format(row['Symbol']))
    if "timestamp" in data.columns:
        df.append(data, ignore_index=True)
        print(df.tail())
        print(df.shape)