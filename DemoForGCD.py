# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 20:07:58 2016

@author: Luke
"""

import pandas as pd 
import numpy as np
import statsmodels.formula.api as smf


Data = pd.read_csv('C:\Users\Luke\Documents\ForSpatialest\PlsWork.csv')
Data['Constant'] = 1
regressors = Data[['Column2', 'Column3', 'Column4', 'Constant']]
response= Data['Column1']
est = smf.OLS(response, regressors)
est = est.fit()
test = 'test123'
#print est.summary().as_html()
returnthis = est.summary().as_html()
#print 'yeoooooo'
