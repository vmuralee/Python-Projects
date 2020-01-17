# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:39:07 2019

@author: Vinay
"""
import copy
import matplotlib.pyplot as plt

# Aitken Method

def Aitken(x_arr,y_arr,x):
    npoint = len(x_arr)
    ftmp=y_arr.copy()
    for j in range(1,npoint):
        for i in range(npoint-j):
            fx = (x-x_arr[i+j])*ftmp[i]/(x_arr[i]-x_arr[i+j])+(x-x_arr[i])*ftmp[i+1]/(x_arr[i+j]-x_arr[i])
            ftmp.append(fx)
        ftmp=ftmp[npoint-j+1:]
    return ftmp[0]
#---- end of Function -----#



xi = [0,0.5,1,1.5,2]
fi = [1,0.938470, 0.765198, 0.511828,0.223891]
xi_fit = [0,0.25,0.5,0.75,1,1.25,1.5,1.75,2]
fi_fit = [fi[0],Aitken(xi,fi,0.25),fi[1],Aitken(xi,fi,0.75),fi[2],Aitken(xi,fi,1.25),fi[3],Aitken(xi,fi,1.75),fi[4]]
plt.plot(xi,fi,'r+')
plt.plot(xi_fit,fi_fit)
plt.show()
