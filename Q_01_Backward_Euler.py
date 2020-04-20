#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:06:04 2020

@author: jaga
"""
# Solution of ODE Using Backward Euler Method

import matplotlib.pyplot as plt
from scipy.optimize import newton
import numpy as np


''' 1st Problem '''

#initial condition
w = np.e
h=0.01

# Empty List to store the x and y(x)
soln=[]
x=[]

# initial value of x=0
t=0
t_f = 1
while t<= t_f + h:   # h is added to to append the y(t_f)
    soln.append(w)
    x.append(t)
    t=t+h
    
    #definition of the function to solve it by Newton-Raphson
    def f(y):
        # its actually in the form  [  y - w - h * dydx(x,y) ]
        return  y - w - h*(- 9 * y)
    
    ''' We may have multiple root of the f(y)=0 equ. but our desired root is
     near the w=y(xi), That's why starting point of this solver is chosen as
     w to get the access the root near w
     '''
    start_point = w
    w=newton(f,start_point)
plt.plot(x,soln,ls='dashed', 
         marker='.', markersize=1,label="computed sol")
plt.xlabel('x',fontsize=13)
plt.ylabel('y(x)', fontsize=13)
plt.title('Solution Using Backward_Euler Method')
plt.legend()
plt.show()


''' 2nd Problem '''

#initial condition
w=1/3.0
h=0.01

# Empty List to store the x and y(x)
soln=[]
x=[]

# initial value of x=0
t=0
t_f = 1
while t<= t_f + h:   # h is added to to append the y(t_f)
    soln.append(w)
    x.append(t)
    t=t+h
    
    #definition of the function to solve it by Newton-Raphson
    def f(y):
        # its actually in the form  [  y - w - h * dydx(x,y) ]
        return  y - w - h*(- 20*(y-t)**2 + 2*t)  
    
    ''' We may have multiple root of the f(y)=0 equ. but our desired root is
     near the w=y(xi), That's why starting point of this solver is chosen as
     w to get the access the root near w
     '''
    start_point = w
    w=newton(f,start_point)
plt.plot(x,soln,ls='dashed', 
         marker='*', markersize=2,label="computed sol")
plt.xlabel('x', fontsize=13)
plt.ylabel('y(x)', fontsize=13)
plt.title('Solution Using Backward_Euler Method')
plt.legend()
plt.show()