#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic class to interpolate a set of points using different techniques
"""
import numpy as np

class Polynomial():
    def __init__(self,steps=10,n=1):
        self.steps = steps
        self.n = n
    
    def calc(self,y1,y2):
        x1_ = -1
        x2_ = 1
        #print(y1)
        x1 = [x1_ for i in range(len(y1))]
        x2 = [x2_ for i in range(len(y1))]
        
        m = (y1-y2)/(x1_-x2_)
        c = y1 - x1_*m
        inner_x = np.linspace(x1,x2,self.steps)**self.n
        inner_y = m*inner_x+c
        return inner_y
    
    def calc_rgb(self,y1,y2):
        y1 = -1
        y2 = 1
        
        pass

if __name__ == '__main__':
    L = Polynomial(10,n=3)
    a=L.calc_rgb(np.array([5,1,2]),np.array([6,6,6]))
          
    for i in a:
        print(i[0])