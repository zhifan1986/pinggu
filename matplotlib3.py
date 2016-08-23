#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from numpy.random import randn

data = 'iris.csv'
iris = pd.read_csv(data)
#iris.head(5)
#iris.ix[:,:-1].hist()
iris.ix[5:,:-1].hist()
iris.corr()
from pandas.tools.plotting import scatter_matrix
scatter_matrix(iris, alpha=0.3,figsize=(6,6), diagonal = 'kde')
iris.plot(kind = 'kde', style = '--')
iris.boxplot()
plt.show()