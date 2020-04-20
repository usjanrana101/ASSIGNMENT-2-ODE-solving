#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:27:24 2020

@author: jaga
"""

'''
  Solution of Second order ODE using RK4 method 
                                                  '''
import matplotlib.pyplot as plt
import numpy as np

# r is an array with r[0]=y and r[1]=z(=dy/dx)
def f(x,r): 
   dydx=r[1]
   dzdx=2*r[1]-r[0]+x*(np.exp(x)-1)
   return np.array([dydx,dzdx])

# initial values of [y , y']
r=np.array([0.0,0.0])  
h=0.001

y_sol=[]
x_sol=[]

x=0 # initial value of x
x_f=1

while x<=x_f + h:    # h is added to to append the y(x_f)
    y_sol.append(r[0])
    x_sol.append(x)
    
    # RK4 formula for the y(x(i+1))
    
    k1=h*f(x,r)
    k2=h*f(x+0.5*h,r+0.5*k1)
    k3=h*f(x+0.5*h,r+0.5*k2)
    k4=h*f(x+h,r+k3)
    
    r=r+(k1+2*k2+2*k3+k4)/6.0
    x=x+h
plt.plot(x_sol,y_sol,label="Numerical solution")
plt.xlabel('x', fontsize=13)
plt.ylabel('y(x)', fontsize=13)
plt.title('Solution Using RK4 Method')
plt.legend()
plt.show()