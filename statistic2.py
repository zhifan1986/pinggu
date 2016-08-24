#!/usr/bin/python
# -*- coding: utf-8 -*-
#filename:

from scipy import stats
from scipy.optimize import leastsq
import pylab as pl
import numpy as np

def func(x, p):
    A, k, theta = p 
    return A*np.sin(2*np.pi*k*x+theta)

def res(p,y,x):
    return y - func(x, p)

x = np.linspace(0, -2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6
y0 =func(x,[A,k,theta])
y1 =y0 + 2*np.random.randn(len(x))

p0 =[7, 0.2, 0]
plsq = leastsq(res, p0,args =(y1,x))
print plsq

pl.plot(x,y0,label = 'T')
pl.plot(x,y1,label = 'S')
pl.plot(x,func(x,plsq[0]),label = 'N')
pl.legend()
pl.show()
    