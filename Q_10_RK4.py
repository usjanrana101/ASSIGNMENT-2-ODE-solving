#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:33:37 2020

@author: jaga
"""


# returns dx/dt(t,x)
def f(t,x):
   return (1/(t*t+x*x))

# initial value of y
w=1
h=1

# final value of t at which we have to get y 
t_f=3.5*(10**6)

# initial value of t
t=0
while t<=t_f+h:
    
    #  RK4 formula
    k1=h*f(t,w)
    k2=h*f(t+0.5*h,w+0.5*k1)
    k3=h*f(t+0.5*h,w+0.5*k2)
    k4=h*f(t+h,w+k3)
    
    w=w+(k1+2*k2+2*k3+k4)/6.0
    t=t+h
print("Value of y(t) at t=",t_f," is= ",w)
