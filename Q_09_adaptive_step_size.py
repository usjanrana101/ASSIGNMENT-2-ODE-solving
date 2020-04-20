#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:55:32 2020

@author: jaga
"""
# adaptive step-size control in RK4 method

import matplotlib.pyplot as plt
import numpy

def f(t,x):
    return (x+x*x)/t

def RK4(t,w,h):  # returns the y(t+h) using RK4 method given y(t)=w
    k1=h*f(t,w)
    k2=h*f(t+0.5*h,w+0.5*k1)
    k3=h*f(t+0.5*h,w+0.5*k2)
    k4=h*f(t+h,w+k3)
    w=w+(k1+2*k2+2*k3+k4)/6.0
    return w

t_f=3.
t0=1.
delta=10**(-4) # accuracy given

w=-2 # initial value of x(t)
h=0.01  # initial value of step_size taken

y_sol=[]
x_sol=[]

t=t0 #initial t
while t<=t_f + h:
   # evaluating y[t+2h] by two step 
  y1 = RK4(t+h , RK4(t,  w , h) , h)
  #evaluating y[t+2h] by a single step 
  y2 = RK4(t , w , 2 * h)
  q = 30 * h * delta/abs(y1 - y2) # decider value
  
  h_new = q**(1/4.) * h
  
  if q**(1/4.)>1:
      h=h_new
      continue
  else:
    h=h_new
    y_sol.append(w)
    x_sol.append(t)
    w=RK4(t , w , h)
  t=t+h
# plotting the exact solution
t=numpy.arange(t0,t_f + 0.1,0.1)
plt.plot(t,2*t/(1 - 2*t),ls='dashed',label="Exact solution") 

plt.plot(x_sol,y_sol,marker='.',markersize=10,label="Numerical solution with Sample Points")

plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solution Using RK4 Method with adaptive step-size control')
plt.legend()
plt.show()