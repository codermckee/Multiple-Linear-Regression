# -*- coding: utf-8 -*-
from numpy import genfromtxt
import numpy as np
from sklearn import linear_model

data = genfromtxt('data.csv',delimiter = ',')


X = data[:,0:-1]
Y = data[:,-1]

print 'X'
print X
print 'Y'
print Y

regression_equation = linear_model.LinearRegression()
regression_equation.fit(X,Y)

print '系数为'
print regression_equation.coef_
print '截面或截距为'
print regression_equation.intercept_

testX = [1,0,0,28,1]
predict = regression_equation.predict(testX)
print '预测结果为：',predict



