#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename:

import pylab
from scipy import stats

import numpy as np



x = np.array([1,2,5,7,10,15])
y = np.array([2,6,7,9,14,19])
slope, intercept, r_value, p_value, slope_std_err = stats.linregress(x, y)
predict_y = intercept + slope * x 
pred_error = y - predict_y
degree_of_freedom = len(x)-2
residual_std_error = np.sqrt(np.sum(pred_error**2)/degree_of_freedom)

print stats.linregress(x,y), degree_of_freedom, residual_std_error
pylab.plot(x,y,'o')
pylab.plot(x,predict_y,'k-')
pylab.show()