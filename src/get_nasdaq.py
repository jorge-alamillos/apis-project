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

#Download Nasdaq stock quote data from Yfinance library
def import_nsdq():
    global nsdq
    '''
    Import Nasdaq data using from Yahoo Finance using Yfinance library
    '''
    nsdq = yf.download("NDAQ", start="2010-03-01", end="2020-09-13").drop(columns="Adj Close").reset_index().rename(columns={
                                                                                                                            "Open":"Open_Nsdq",
                                                                                                                            "Close":"Close_Nsdq",
                                                                                                                            "High":"High_Nsdq",
                                                                                                                            "Low": "Low_Nsdq",
                                                                                                                            "Volume":"Volume_Nsdq"})
    print("Nasdaq data downloaded!")
    return nsdq

#Export Nasdaq data to csv
def nsdq_csv():
    print("Nsdq.csv exported!")
    return nsdq.to_csv("files/nsdq.csv")


