
import numpy as np
import pandas as pd
import os
import datetime
import plotly.graph_objects as go
import psutil
import dataframe_image as dfi
import re

def import_df():
    global apns
    apns = pd.read_csv("aaplNsdq.csv")
    print ("df imported!")
    return apns

def candle_dates(select,dateFrom,dateTo):
    select = apns[(apns["Date"]< dateTo) & (dateFrom < apns["Date"])]
    fig = go.Figure(data=[go.Candlestick(x=select['Date'],
                    open=select['Open_Aapl'], high=select['High_Aapl'],
                    low=select['Low_Aapl'], close=select['Close_Aapl'])
                        ])
    fig.update_layout(xaxis_rangeslider_visible=False, 
                    title='Evolución de las acciones de Apple',
                    yaxis_title='Acciones AAPL')
    print("candleplot exported as candleplot.png!")
    
    fig1 = go.Figure()
    fig1.add_scatter(x=select['Date'], y=select['Close_Aapl'], mode='lines', name="Apple")
    fig1.add_scatter(x=select['Date'], y=select['Close_Nsdq'], mode='lines', name="Nasdaq-100")
    fig1.update_layout(
                    title='Evolución de las acciones de Apple frente al NASDAQ-100',
                    yaxis_title='Cotización')
    fig.write_image("output/lineplot.png")
    print("lineplot exported as lineplot.png!")
    return fig.write_image("output/candleplot.png"), fig1.write_image("output/lineplot.png")

def df_stats(select):
    x = select.describe()[["Open_Aapl","Close_Aapl","Volume_Aapl"]]
    x["Volume_Aapl"] = x["Volume_Aapl"].map('{:,.2f}'.format)
    x["Open_Aapl"] = x["Open_Aapl"].map('{:,.2f}'.format)
    x["Close_Aapl"] = x["Close_Aapl"].map('{:,.2f}'.format)
    return dfi.export(x, 'output/statistics.png')

def models(dateFrom,dateTo):
    modelos = pd.read_csv("src/files/intro_dates.csv")
    x = modelos[(modelos["Date"]<= dateTo) & (modelos["Date"] >= dateFrom)]
    return dfi.export(x, 'output/models.png' )

def import_model(model):
    date = pd.read_csv("src/files/intro_dates.csv")
    date = date[date["Model"] == model]["Date"]
    return date

def pres_date(date):
    d = str(date)
    d = re.findall(r"\d{4}-\d{2}-\d{2}",d)
    for i in d:
        pres_date = str(i)
    return pres_date

def pres_year(date):
    x = str(date)
    y = re.findall(r"\d{4}",x)
    for i in y:
        year = int(i)
    return year

def model_from(year):
    dateFrom = f"{year}-01-01"
    return dateFrom  
    
def model_to(year):
    dateTo =f"{year+1}-01-01" 
    return dateTo


def candle_model(select,dateFrom,dateTo,model,pres_date):
    select = apns[(apns["Date"]< dateTo) & (dateFrom < apns["Date"])]
    fig = go.Figure(data=[go.Candlestick(x=select['Date'],
                    open=select['Open_Aapl'], high=select['High_Aapl'],
                    low=select['Low_Aapl'], close=select['Close_Aapl'])
                        ])
    fig.update_layout(xaxis_rangeslider_visible=False, 
                    title='Evolución de las acciones de Apple',
                    yaxis_title='Acciones AAPL',
                    shapes = [dict(
                    x0=pres_date, x1=pres_date, y0=0, y1=1, xref='x', yref='paper',
                    line_width=2)],
                    annotations=[dict(
                    x=pres_date, y=0.05, xref='x', yref='paper',
                    showarrow=False, xanchor='left', text=f'Presentación del {model}')])
    print("candleplot exported as lineplot.png!")
    return fig.write_image("output/candleplot.png")

def line_model(select,dateFrom,dateTo,model,pres_date):
    fig = go.Figure()
    fig.add_scatter(x=select['Date'], y=select['Close_Aapl'], mode='lines', name="Apple")
    fig.add_scatter(x=select['Date'], y=select['Close_Nsdq'], mode='lines', name="Nasdaq-100")
    fig.update_layout(
        title='Evolución de las acciones de Apple frente al NASDAQ-100',
        yaxis_title='Cotización',
        shapes = [dict(
            x0=pres_date, x1=pres_date, y0=0, y1=1, xref='x', yref='paper',
            line_width=2)],
        annotations =[dict(
            x=pres_date, y=0.35, xref='x', yref='paper',
            showarrow=False, xanchor='left', text=f'Presentación del {model}')])
    print("lineplot exported as lineplot.png!")
    return fig.write_image("output/lineplot.png")


