# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:15:09 2020

@author: noahs
"""

import pandas as pd
import numpy as np
import math



def __init__():
    pass

def clean_Data(df, n_Points, x_Name, Y_Name, xconvert, yconvert):
    print(df.columns)
    #df = df[[x_Name, Y_Name]]
    df = df.loc[:n_Points]
    if xconvert == True:
        df.loc[:,x_Name] = convert(df.loc[:,x_Name])
    else:
        df.loc[:,x_Name] = df.loc[:,x_Name].map(lambda x: float(x))
    if yconvert == True:
        df.loc[:,Y_Name] = convert(df.loc[:,Y_Name])
    else:
        df.loc[:,Y_Name] = df.loc[:,Y_Name].map(lambda y: float(y))

    #df = df[x_Name,Y_Name].replace(0, np.NaN).dropna()
    df.index = range(0,len(df))
    return df





def lambda_Func(x):
    if 'M' in x:
        return float(x.lstrip('€').rstrip('M'))*1000000
    if 'K' in x:
        return float(x.lstrip('€').rstrip('K'))*1000
     
def convert(col):   
    col = col.map(lambda x: lambda_Func(x))
    return col



def avg_Point(x, y):
    size = len(x)

    x_Total, y_Total = 0,0
    for i in x:     
        x_Total+=i
    for j in y:
        y_Total+=j
    return (x_Total/size, y_Total/size)

def SS(x,Y,m,b):
    sum = 0
    for i in range(len(x)):
        sum+= math.pow(Y[i]-linear(x[i], m,b), 2)
    return sum
    

    
def linear(x,m,b):
    return m*x + b



def sum_xy(x,Y):
    sum = 0
    counter = 0
    for i in x: 
        sum+=i*Y[counter]
        counter+=1
    return sum

def sum_x(x):
    sum = 0
    for i in x:
        sum+=i
    return sum        

def sum_y(Y):
    sum = 0
    for i in Y:
        sum+=i
    return sum        

def sum_y2(Y):
    sum = 0
    for i in Y:
        sum+=(i*i)
    return sum

def sum_x2(x):
    sum = 0
    for i in x:
        sum+=(i*i)
    return sum


    