#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:51:05 2020

@author: jaga
"""

import matplotlib.pyplot as plt
import numpy as np

# r is an array with r[0]=y and r[1]=z(=dy/dt)
def f(t,r): 
   dydt=r[1]
   dzdt=(2/t)*(r[1]-r[0]/t)+t*np.log(t)
   return np.array([dydt,dzdt])

def true_sol(t):
    return 7*t/4. + ((t**3)*np.log(t))/2. - 3*(t**3)/4.

# initial values of y and y'
r=np.array([1.0,0.0])  
h=0.001

y_sol=[]
abs_err=[]

t_sol=[]
t=1.0 # initial value of x
t_f = 2

while t<=t_f + h:
    y_sol.append(r[0])
    abs_err.append(abs(r[0]-true_sol(t)))
    t_sol.append(t)
    
    r=r+h*f(t,r)
    t=t+h

# array for calculating exact sol
t=np.arange(1,2,h)

plt.plot(t_sol,y_sol,ls = 'dashed',label="computed solution")
plt.plot(t_sol,abs_err,label="absolute error")
plt.plot(t,true_sol(t),label="exact solution")

plt.xlabel('t', fontsize=13)
plt.ylabel('y(t)', fontsize=13)
plt.title('Solution Using Euler Method')
plt.legend()
plt.show()