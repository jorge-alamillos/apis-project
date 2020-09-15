#!/usr/bin/env python

import numpy as np
import pandas as pd
import os
import datetime

def import_df():
    '''
    Imports aapl.csv" and "nsdq.csv"
    '''
    global aapl
    global nsdq
    aapl = pd.read_csv("files/aapl.csv")
    nsdq = pd.read_csv("files/nsdq.csv")
    print("dfs imported!")
    return aapl,nsdq

def clean_df():
    '''
    Cleans data and filters colums in aapl.csv
    '''
    global aapl
    aapl = aapl.drop(columns="Unnamed: 0").rename(columns={
                                "Open":"Open_Aapl",
                                "Close":"Close_Aapl",
                                "High":"High_Aapl",
                                "Low": "Low_Aapl",
                                "Volume":"Volume_Aapl"})
    return aapl

def merge_aapl_nsdq():
    '''
    Merges aapl.csv" and "nsdq.csv into one df" 
    '''
    global sel
    sel = pd.concat([aapl,nsdq],axis=1)
    print("datasets merged!")
    return sel

def aaplNsdq_csv():
    '''
    Exports Apple-Nasdaq data to csv
    '''
    print("aaplNsdq.csv generated!")
    return sel.to_csv("src/files/aaplNsdq.csv")
import_df()
clean_df()
merge_aapl_nsdq()
aaplNsdq_csv()