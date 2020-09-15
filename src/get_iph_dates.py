
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

def import_dates():
    '''
    Web scrappes iPhone introduction dates from the website
    '''
    global soup
    response = requests.get("https://lamanzanamordida.net/tutoriales/iphone/lanzamiento-iphone-fechas-todos-modelos/")
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Dates imported!")
    return soup

def clean_models():
    '''
    Create models columns
    '''
    global models
    models = pd.DataFrame([tag.text for tag in soup.find_all('h3')]).rename(columns={0:"Model"}).reset_index()
    print("Models column created!")
    return models

def clean_dates():
    '''
    Creates and cleans date column
    '''
    global dates
    data_raw = [tag.text for tag in soup.select('ul li')]
    dates = pd.DataFrame(data_raw[53:151])
    dates = dates[0].str.split(":",expand=True)
    dates = dates[dates[0].str.contains("Fecha de presentación")]
    dates = dates.reset_index(drop=True).drop(columns=[0]).rename(columns={1:"Date"})
    dates = dates.reset_index()
    print("Dates column cleant!")
    return dates


def merge_mod_dat():
    '''
    Merges dates and models columns into a df
    '''
    global intro
    intro =  pd.merge(models,dates,on="index").drop(columns=["index"]).set_index("Model")
    print("Df Models-Date merged!")
    return intro

def clean_intro():
    '''
    Cleans data in intro df
    '''
    global intro
    intro = intro.replace(r"de|\.|\.\.|\s","",regex=True)
    intro['ano'] = intro['Date'].str.extract('(\d{4}$)')
    intro['mes'] = intro['Date'].str.extract('(\D+)')
    intro['dia'] = intro['Date'].str.extract('(\d+)')
    intro = intro.replace({'mes':{'enero': '01',
                                'marzo': '03',
                                'abril': '04',
                                'junio': '06',    
                                'septiembre': '09',
                                'octubre': '10'}}) 
    intro['Date'] = intro["ano"]+"-"+intro["mes"]+"-"+intro["dia"]
    intro = intro.drop(columns=["ano","mes","dia"])
    intro["Date"] = intro["Date"].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))   
    print("Models-Date cleant!")
    return intro

def intro_csv():
    '''
    Exports Nasdaq data to csv
    '''
    print("intro_dates.csv generated!")
    return intro.to_csv("files/intro_dates.csv")
