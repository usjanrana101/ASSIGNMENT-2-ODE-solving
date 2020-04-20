#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:57:53 2020

@author: jaga
"""
'''
  Solution of 2nd order boundary value problem using scipy.integrate.solve_bvp
  '''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp

'''
this function takes d2y/dt2 = f(t,y) , boundary condition given at
t0 and tf ,initial and final value 
of t and y, as t0 and tf.....and y0=y[t0] , yf=y[tf]

'''
def diff_sol_bvp(f ,bc ,t0 ,tf ,y0 ,yf):
    
    # initial mesh points
    x=np.linspace(t0 , tf , 5)
    
    # initially choosen y'(t) in the y[1] array
    # and initial guess of y in the y[0]
    y=np.zeros((2 , x.size)) + 1
    
    sol_bvp = solve_bvp(f, bc, x, y)
    
    x_plot = np.linspace(t0 , tf , 100)
    y_plot=sol_bvp.sol(x_plot)[0]
    
    plt.plot(x_plot, y_plot,label='numerical solution')
    plt.legend()
    plt.xlabel("t", fontsize=13)
    plt.ylabel("y(t)", fontsize=13)
    plt.show()
    
''' 1st problem '''

t0 , tf = 1 , 2
y0 , yf =0 , np.log(2)
def f(x,y):
    
    # y is an array with y[0]=y and y[1]=z(=dy/dt)
    return np.array([y[1],-np.exp(-2*y[0])])

def bc(ya, yb):
    return np.array([ya[0] - y0 , yb[0] - yf])

diff_sol_bvp(f ,bc ,t0 ,tf ,y0 ,yf)
\

''' 2nd problem '''

t0 , tf = 0 , (np.pi)/2.
y0 , yf =1 , np.e
def f(x,y):
    return np.array([y[1], y[1]*np.cos(x) - y[0]*np.log(y[0])])

def bc(ya, yb):
    return np.array([ya[0] - y0 , yb[0] - yf])

diff_sol_bvp(f ,bc ,t0 ,tf ,y0 ,yf)


''' 3rd problem '''

t0 , tf = (np.pi)/4. , (np.pi)/3.
y0 , yf =2**(-0.25) , 0.5*(12**(0.25))
def f(x,y):
    return np.array([y[1], - (2 * y[1]**3 + y[0]**2 * y[1]) /np.cos(x) ])

def bc(ya, yb):
    return np.array([ya[0] - y0 , yb[0] - yf])

diff_sol_bvp(f ,bc ,t0 ,tf ,y0 ,yf)


''' 4th problem '''

t0 , tf = 0 , np.pi
y0 , yf = 2 , 2
def f(x,y):
    return np.array([y[1], 0.5 - 0.5 * y[1]**2 - 0.5 * y[0] * np.sin(x)])

def bc(ya, yb):
    return np.array([ya[0] - y0 , yb[0] - yf])

diff_sol_bvp(f ,bc ,t0 ,tf ,y0 ,yf)