# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:10:20 2020

@author: noahs
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import Regress as r
import func
m,b = 0,0
fig, (ax1,ax2 )= plt.subplots(2, 1)

def scatter_Plot(x, Y, all_L, avg_L, avgP, x_L,y_L ):

    
    ax1.scatter(x,Y, label = all_L, s = 5, c = 'b')
    ax1.scatter(avgP[0],avgP[1], label = avg_L, s = 25, c = 'r')    
    ax1.set(title = 'Fifa Data Set', xlabel = x_L, ylabel = y_L)
    fig.set_size_inches(12,12)
    ax1.legend()
    #bs = np.linspace(model.get_m()-2*model.get_m(),model.get_m()+2*model.get_m())
    slopes = np.arange(model.get_m()-2*model.get_m(),model.get_m()+2*model.get_m(),model.get_m()/5)

    SSs = []
    print('Please wait...')
    for i in range(len(slopes)):
        SSs.append(func.SS(x,Y,slopes[i], avgP[1] - slopes[i]*avgP[0]))
    ax2.plot(slopes, SSs)
    ax2.set(title = 'Sum of Squared Error', xlabel = 'Slope', ylabel = 'SS')
def line_Plot(x):
    x = np.linspace(0,np.max(x))
    ax1.plot(x, m*x+b, c = 'y')


colx = 'Overall'    #choose columns to compare
colY = 'Potential'

Odf = pd.read_csv('data.csv')    #import data set
df = Odf.loc[:,'Crossing':'GKReflexes']
df = pd.concat([df, Odf.loc[:,['Overall','Potential']]], axis = 1)
i = 100000     #number of points to compare
clean_df = func.clean_Data(df,i,colx, colY,False, False)    #Clean the data

x = clean_df[colx] 
Y = clean_df[colY] 



model = r.best_Fit()    #Create a best fit model
model.fit(x, Y)     #Fit with the data


m = model.slope_Best()  #Use model to find slope of best fit line
b = model.b_Best()  #Use model to find y intercept of best fit line
avgP = model.get_avgP() #Get the average point


scatter_Plot(x,Y, 'Individual',  'Average individual',avgP, colx, colY )
line_Plot(x)


print('\n\nThe best fit line for this set of data is: y =', m, 'x +', b )
