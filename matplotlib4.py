#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from numpy.random import randn
from IPython.core.pylabtools import figsize

labels = []
quants = []

for line in file('major_country_gdp.txt'):
    info = line.split()
    labels.append(info[0])
    quants.append(float(info[1]))
plt.figure(1,figsize(6,6))

def exp(label,target='USA'):
    if label == target:
        return 0.1
    else:
        return 0
    
expl = map(exp, labels)
colors = ['pink','red','yellow','green','orange','blue','violet','indigo','purple']
plt.pie(quants,
        explode = expl,
        labels = labels,
        autopct = "%1.2f%%",
        pctdistance = 0.8,
        shadow = True)
plt.title("Top 10 GDP Countries", bbox= {'facecolor':'0.8','pad':'0.5'})
plt.legend()
plt.show()
    
