#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename:

import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from numpy.random import randn

s = Series(np.random.randn(10).cumsum(),index = np.arange(1,100,10))
s.plot
plt.plot(s)
plt.show()

df = DataFrame(np.random.randn(10,4).cumsum(0),
               index = np.arange(0,100,10),
               columns = ['A', 'B', 'C', 'D'])
df.plot()
plt.show()
df.plot(kind = 'bar', stacked = False)
plt.show()