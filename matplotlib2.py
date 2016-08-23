#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from numpy.random import randn
from pandas.tools.plotting import scatter_matrix

url = "http://s3.amazonaws.com/assets.datacamp.com/course/dasi/present.txt"
present = pd.read_table(url, sep= ' ')
present_year = present.set_index('year')
present_year.plot(x = 'boys', y= 'girls',kind = 'scatter')

scatter_matrix(present, alpha= 0.2,diagonal='kde')
plt.show()