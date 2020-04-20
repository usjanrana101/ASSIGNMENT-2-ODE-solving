#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:56:04 2020

@author: jaga
"""
'''
    Solution of ODE by Forward Euler Method
    '''
import matplotlib.pyplot as plt
import numpy as np

# definition of dy/dt(y,t)

def f(t,y):
   return (y/t)*(y/t-1)
def true_sol(t):
    return t/(1+np.log(t))

#  initial value
w=1
h=0.1

# empty lists to store the desired values
soln=[]
x=[]
abs_err=[] 
rel_err=[]

t=1
t_f = 2

while t<=t_f + h:  # h is added to to append the y(t_f)
    soln.append(w)
    x.append(t)
    
    # appending the errors
    abs_err.append(abs(w-true_sol(t)))
    rel_err.append(abs(w-true_sol(t))/true_sol(t))
    
    # Formula for Forward Euler Method
    w=w+h*f(t,w)
    t=t+h

# an array to plot the exact solution
t=np.arange(1,2,0.01)

plt.plot(x,soln,ls='dashed', 
         marker='*', markersize=5,label="Numerical solution")

plt.plot(x,abs_err,ls=':', 
         marker='o', markersize=5,label="Absoute error")

plt.plot(x,rel_err,ls=':', 
         marker='<', markersize=5,label="Relative error")

plt.plot(t,true_sol(t),label="Exact solution")

plt.xlabel('t', fontsize=13)
plt.ylabel('y(t)', fontsize=13)
plt.title('Solution Using Euler Method')
plt.legend(loc=6)
plt.show()