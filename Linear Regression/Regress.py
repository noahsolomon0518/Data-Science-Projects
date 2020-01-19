# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:42:04 2020

@author: noahs
"""


#import pandas
import math
import pandas as pd
import numpy as np
import func


class best_Fit:
    def __init__(self):
        
        self.df = 0
        self.x = 0
        self.Y = 0
        self.size = 0
        self.avgP = 0
        self.slope = 0
        self.b = 0
        
    def fit(self,x,Y):
        self.x = x
        self.Y = Y
        self.size = len(x)
        self.avgP = func.avg_Point(x,Y)  
    
    
    def slope_Best(self):
        n = self.size
        xy = func.sum_xy(self.x, self.Y)
        x = func.sum_x(self.x)
        y = func.sum_y(self.Y)
        x2 = func.sum_x2(self.x)
        avgx = self.avgP[0]
        avgy = self.avgP[1]
        self.slope = ((-2*xy)+(2*avgx*y)+(2*avgy*x)-(2*n*avgx*avgy))/((4*avgx*x)-(2*n*avgx**2)-(2*x2))
        return self.slope
    
    def b_Best(self):
        
        avgx = self.avgP[0]
        avgy = self.avgP[1]
        self.b = (avgy - self.slope*avgx)
        return self.b
    
    
    def get_b(self):
        return self.b
    
    def get_m(self):
        return self.slope
    
    def get_avgP(self):
        return self.avgP

