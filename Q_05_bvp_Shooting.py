#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:05:21 2020

@author: jaga
"""
''' 
    Boundary Value Problem using Shooting Method
                                                '''
                                                
import numpy as np
import matplotlib.pyplot as plt

# empty list to store candidate sols for different guessed y'[x_init]
candidate_sol=[]

# stores the y(x_f) for different chosen v=y'[0]
y_v=[] 
g=10

# r is an array with r[0]=y and r[1]=z(=dy/dx)
def f(x,r): 
   dydx=r[1]
   dzdx=-g
   return np.array([dydx,dzdx])

''' v=y'[0] and we are calculating the solutions for each value and appending 
   the whole solution set to the candidate_sol list
                                                 '''
for v in np.arange(40.,60.,1):
    # a list to store the y's for a particular v
    trial_sol=[]
    
    # initial values y[0]=0,and y'[0]=v
    x_i = 0
    r=np.array([x_i,v])  
    h=0.001
    
    x=0 # initial value of x
    x_f=10
    
    x_sol=[]
    while x<=x_f+h:
       y_xf=r[0]  # this actually stores the y[x_f] before leaving the loop
       
       trial_sol.append(r[0])
       x_sol.append(x)
       
       # RK4 formula
       k1=h*f(x,r)
       k2=h*f(x+0.5*h,r+0.5*k1)
       k3=h*f(x+0.5*h,r+0.5*k2)
       k4=h*f(x+h,r+k3)
       
       r=r+(k1+2*k2+2*k3+k4)/6.0
       x=x+h
       
    y_v.append(y_xf)
    candidate_sol.append(trial_sol)

# converting it to array for calculating the exact sol formula and also for argmin    
y_v=np.array(y_v)
x_sol=np.array(x_sol)

act_y_xf = 0 # it is the given value of y at x_f 

'''return the index of y_v where the computed valye at x_f is closest to given
    2nd bondary condition'''
index_of_min = np.argmin(abs(y_v - act_y_xf))

# at that index of candidate_sol the list is our desired sol data matched with bc
plt.plot(x_sol,candidate_sol[index_of_min],
           ls='dashed',label="numerical solution")

plt.plot(x_sol,-0.5*g*x_sol*x_sol + 50*x_sol, ls=':', label="exact solution")

for i in range(index_of_min - 10, index_of_min + 10 , 3):
    plt.plot(x_sol,candidate_sol[i],label="candidate solution")
    
plt.xlabel('x', fontsize=13)
plt.ylabel('y(x)', fontsize=13)
plt.xlim(0.,10.)
plt.ylim(0.,400.)
plt.title('Solution Using Shotting Method')
plt.legend()
plt.show()