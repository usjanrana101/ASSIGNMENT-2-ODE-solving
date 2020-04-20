#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:51:39 2020

@author: jaga
"""

''' Solution of some ODE's using the solve_ivp() function '''

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

'''
this function takes dy/dt = f(t,y) , exact_sol(t) ,initial and final value 
of t as t0 and tf.....and y0=y[t0]
and the step size h

To argue why the given solution of the diff equ. by using 
scipy.integrate.solve_ivp() gives correct result..
we plot the exact solution and absolute error ....

both matches perfectly....
'''
def diff_sol_ivp(f , exact_sol ,t0 ,tf, y0, h):
    
    t_evaluation=np.arange(t0,tf,h)
    
    # solution using scipy.integrate.solve_ivp()
    soln=solve_ivp(f,[t0,tf],[y0],t_eval=t_evaluation)
    
    # soln[0] = array of functional value at the mesh points returned by scipy.integrate.solve_ivp()
    plt.plot(t_evaluation,soln.y[0],label="Numerical Solution")
    plt.plot(t_evaluation,exact_sol(t_evaluation),label="Exact Solution")
    plt.plot(t_evaluation,abs(exact_sol(t_evaluation)-soln.y[0]),label="Absolute Error")
    
    plt.xlabel('t', fontsize=13)
    plt.ylabel('y(t)', fontsize=13)
    plt.title('Solution Using solve_ivp()')
    plt.legend()
    plt.show()

''' 1st Problem '''

def f(t,y):
    return t*(np.exp(3*t))-2*y
def exact_sol(t):
    return np.exp(3*t)*(t-0.2)/5.0+np.exp(-2*t)/25.0
t0=0.0
tf=1.0
y0=0.0
h=0.01

# calling the diff_sol_ivp() for solving this example
diff_sol_ivp(f , exact_sol ,t0 ,tf, y0, h)


''' 2nd problem '''

def f(t,y):
    return 1 - (t-y)**2 
def exact_sol(t):
    return t + 1/(t-3.0)
t0=2.0
tf=3.0
y0=1.0
h=0.01

# calling the diff_sol_ivp() for solving this example
diff_sol_ivp(f , exact_sol ,t0 ,tf, y0, h)

''' 3rd problem '''

def f(t,y):
    return 1+(y/t)
def exact_sol(t):
    return 2*t+t*np.log(t)
t0=1.0
tf=2.0
y0=2.0
h=0.01

# calling the diff_sol_ivp() for solving this example
diff_sol_ivp(f , exact_sol ,t0 ,tf, y0, h)

''' 4th problem '''

def f(t,y):
    return np.cos(2*t)+np.sin(3*t)  
def exact_sol(t):
    return np.sin(2*t)/2.0 - np.cos(3*t)/3.0 + 4/3
t0=0.0
tf=1.0
y0=1.0
h=0.01

# calling the diff_sol_ivp() for solving this example
diff_sol_ivp(f , exact_sol ,t0 ,tf, y0, h)