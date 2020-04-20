#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:35:16 2020

@author: jaga
"""

'''   Solution of system of first order initial value ODE's using RK4 method '''

import matplotlib.pyplot as plt
import numpy as np

 # r is an array with r[0]=u1(t) and r[1]=u2(t) and r[2]=u3(t)
def f(t,r):
   du1dt=r[0]+2*r[1]-2*r[2]+np.exp(-t)
   du2dt=r[1]+r[2]-2*np.exp(-t)
   du3dt=2*r[1]-2*r[2]+np.exp(-t)
   return np.array([du1dt,du2dt,du3dt])

# initial values of u1,u2,u3
r=np.array([3.0,-1.0,1.0])
h=0.001

# Empty lists to store the functional values
u1=[]
u2=[]
u3=[]

# empty list to store the t values for plotting
t_sol=[]

# initial value of t
t=0.0
t_f = 1
while t<=t_f + h:  # h is added to to append the u(t_f)
    u1.append(r[0])
    u2.append(r[1])
    u3.append(r[2])
    t_sol.append(t)
    
    k1=h*f(t,r)
    k2=h*f(t+0.5*h,r+0.5*k1)
    k3=h*f(t+0.5*h,r+0.5*k2)
    k4=h*f(t+h,r+k3)
    
    r=r+(k1+2*k2+2*k3+k4)/6.0
    t=t+h

plt.plot(t_sol,u1,label="u1(t)")
plt.plot(t_sol,u2,label="u2(t)")
plt.plot(t_sol,u3,label="u3(t)")

plt.xlabel('t', fontsize=13)
plt.ylabel('u(t)', fontsize=13)
plt.title('Solution Using RK4 Method')
plt.legend()
plt.show()