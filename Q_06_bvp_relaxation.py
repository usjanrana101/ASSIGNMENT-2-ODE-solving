#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:41:22 2020

@author: jaga
"""

''' relaxation method for solving bvp
                                     '''
import numpy as np
import matplotlib.pyplot as plt
candidate_sol=[]

g=10.

# given boundary condition..
x0=0.
xf=10.
y_x0=0.
y_xf=0.

# choosen mesh point no = N
mesh_pts_no=100
h=(xf - x0)/(mesh_pts_no + 1)

# x_sol contains N+2 points including x0 and xf
x_sol=[]
for i in range(mesh_pts_no+2):
    x_sol.append(x0 + i*h)
x_sol=np.array(x_sol)

# matrix constructing like A= [[0,1,0,0,0]
#                              [1,0,1,0,0]
#                              [0,1,0,1,0]
#                              [0,0,1,0,1]
#                              [0,0,0,1,0]
#                                         ]n*n
A=np.zeros((mesh_pts_no,mesh_pts_no))
for i in range(mesh_pts_no):
    if i == 0:
        A[i][i+1]=1
    elif i == mesh_pts_no-1:
        A[i][i-1]=1
    else:
        A[i][i+1]=1
        A[i][i-1]=1

'''
     Now let me clear the algorithm used here .....
     as x=f(x) can be solved by relaxation using initial guess x=x0 and updating it 
     by x=f(x0) and then iterating this process..assuming this function fullfill
     the convergence criteria for getting true sol..
     now, here for this given problem..
       the euation is like  Y = AY + constant
       where Y = [y(x1),y(x2)....,y(xN)] , and A is the constructed matrix
       and constant is being construced below...
       For different linear ODE problem only A and constant matrix will change 
        
       Chossing the initial value of the Y i.e y_xi ...solution is converging 
       towards the true sol..
      '''

y_xi=np.zeros(mesh_pts_no) + 0.1  # initial guess

  #  constructing the constant matrix = 0.5*[gh^2-x0,gh^2,gh^2.....,gh^2,gh^2-xf]
constant=np.zeros(mesh_pts_no) + 0.5 * g*h*h
constant[0]=constant[0] + y_x0/2.     
constant[mesh_pts_no - 1]=constant[mesh_pts_no - 1] + y_xf/2.

# storing the previous value of the functionl values to check the accuray
y_xi_prev=np.zeros(mesh_pts_no) + 1
index=0  # to track the solutions

added_y_xi=np.insert(y_xi,(0,mesh_pts_no),(x0,xf))

exact_sol=(-0.5*g*x_sol*x_sol + 50*x_sol)

while (max(abs(y_xi - y_xi_prev)) >= 0.001):  # choosen accuracy
    index=index+1
    y_xi_prev=y_xi 
    y_xi=0.5*np.dot(A,y_xi) + constant  # update the y_xi
    added_y_xi=np.insert(y_xi,(0,mesh_pts_no),(x0,xf))
    candidate_sol.append(added_y_xi)

plt.plot(x_sol,added_y_xi,
           ls='dashed',label="numerical solution")

plt.plot(x_sol,-0.5*g*x_sol*x_sol + 50*x_sol, ls=':', label="exact solution")

for i in range(index-8000,index-1000,1000):
    plt.plot(x_sol,candidate_sol[i],label="candidate solution")

plt.xlabel('x', fontsize=13)
plt.ylabel('y(x)',fontsize=13)
plt.xlim(0.,10.)
plt.ylim(0.,250.)
plt.title('Solution Using Relaxation Method')
plt.legend()
plt.show()