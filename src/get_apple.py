#!/usr/bin/env python

import json
import re
import requests
import numpy as np
import pandas as pd
from pandas import json_normalize
import os
from dotenv import load_dotenv
load_dotenv()
import datetime
import yfinance as yf


#In this first part, we import the Apple dataset with stocks data from 2010 to feb 2020 

def import_dataset():
    '''
    Imports the dataset file manually downloaded from Kaggle
    '''
    csv = "datasets_533900_976925_HistoricalQuotes.csv"
    global aaplFeb20
    aaplFeb20 = pd.read_csv(csv, index_col= [0], parse_dates=True).reset_index()
    print("csv imported!")
    return aaplFeb20

def filter_col():
    '''
    Filter and correct column names
    '''
    global aaplFeb20
    aaplFeb20 = aaplFeb20[["Date"," Open"," Close/Last",
                           " High"," Low", " Volume"]].rename(columns={
                                                                        " Close/Last":"Close",
                                                                        " Open":"Open",
                                                                        " High":"High",
                                                                        " Low":"Low",
    
                                                                        " Volume":"Volume"})
    print("columns corrected!")
    return aaplFeb20

def clean_kggl():
    '''
    Converts numbers to float and deletes wrong data
    '''
    clmns= ['Open','Close','High','Low']
    for col in clmns:
        aaplFeb20[col] = aaplFeb20[col].str.replace('$', '').astype('float')
    print("data cleant!")
    return aaplFeb20

#From here, we import the 2020 Apple Stocks from IEX API 

def api_dwnld():
    '''
    Generates the API url, makes the request and parses the response into text
    '''
    global data
    baseUrl = "https://cloud.iexapis.com/stable/"
    symbol = "aapl"
    range = "ytd"
    endpoint = f"stock/{symbol}/chart/{range}"#cotización de la empresa
    token = f"?token={os.getenv('token')}"
    url = f"{baseUrl}{endpoint}{token}" 
    response = requests.get(url)
    data = json.loads(response.text)
    print("Url generated!")
    return url
     
def clean_api():
    '''
    Transforms data to df, filters and renames columns
    '''
    global aaplYTD
    aaplYTD = pd.DataFrame(data)
    aaplYTD = aaplYTD[aaplYTD["date"]>"2020-02-28"]
    aaplYTD = aaplYTD[["date","uOpen","uClose","uHigh","uLow", "uVolume"]].rename(columns={"date":"Date",
                                                                                     "uClose":"Close",
                                                                                     "uOpen":"Open",
                                                                                     "uHigh":"High",
                                                                                     "uLow":"Low",
                                                                                     "uVolume":"Volume"})
    print("Data downloaded from API!")
    return aaplYTD

#The function below concatenates Apple Shares price from the API and from Kaggle 
def concat():
    '''
    Concatenates both datasets
    '''
    global aapl
    aapl = pd.concat([aaplFeb20,aaplYTD])
    print("Datasets concatenated!")
    return aapl

def clean_aapl():
    '''
    Cleans Date column 
    '''
    global aapl
    aapl["Date"] = aapl["Date"].apply(lambda x: str(x))
    aapl = aapl.sort_values("Date").reset_index(drop=True).replace(r"00:00:00$|\s","",regex=True)
    aapl["Date"] = aapl["Date"].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
    print("columns cleant!")
    return aapl

#Export Apple data to csv
def aapl_csv():
    print("aapl.csv exported!")
    return aapl.to_csv("files/aapl.csv")

