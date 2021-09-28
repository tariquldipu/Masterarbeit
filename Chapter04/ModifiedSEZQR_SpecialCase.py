#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This simple program tries to solve the ODE of the Modified SEZQR model- Special Case 01 with perturbation
    and create a numerical solution.
    After that, this program draws the solution graph for the Zombie, Quarantined and Removed
    Population. This simple graph helps us to understand the actual scenario of the population
    from the modified SEZQR model- Special Case 01 after a certain number of days.

   Part of MS Thesis at Universität Koblenz-Landau
   Note: this program uses the following libraries-  Numpy, Matplotlib, Scipy
   Python Version 3.7
"""

# MODIFIED SEZQR MODEL- SPECIAL CASE 01

# importing libraries
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
figure(figsize=(6, 6), dpi=150)

# I'm using this style for a pretier plot, but it's not actually necessary
plt.style.use('ggplot')

# Parameter values
beta = 0.0095
alpha = 0.005
zeta = 0.0001
rho = 0.005
kappa = 0.001
sigma = 0.001
gamma = 0.0001
kappa = 0.0001
omega = 0.009
N = 1000  # initial population

# Perturbation Parameter Mu, change this value to see different results
mu = 0.175

# Defining Function of the SEZQR ODE
def model(t, x):
    Z = x[0] # zombies
    Q = x[1] # quarentined
    dzdt = zeta*(N - Z - Q) + omega*Q # Zombies
    dqdt = - gamma*Q - omega*Q # Quarantined
    dxdt = [dzdt, dqdt]
    return dxdt

# Initial Condition. Zombie= 130, Quarantined = 70
x0 = [130, 70]

# Time, as in number of days. Total days= 1000
t = np.array([0, 50000])
tspan = np.linspace(t[0], t[1], 50000)

# Calculating numerical solution of the given ODEs
x = solve_ivp(model, t, x0, t_eval=tspan)

time = x.t
zombie = x.y[0]
quarantined  = x.y[1]
removed = (N - zombie - quarantined)

# Plot
plt.plot(time, zombie, 'r--', label="Zombie") # Zombie Population Graph
plt.plot(time, removed, 'g-.', label="Removed") # Recovered Population Graph
plt.plot(time, quarantined , 'm:', label="Quarantined")
plt.title('Special Case 01 for t = 50000 days')
plt.ylabel('Population')
plt.xlabel('Time (Days)')
plt.legend(loc='best')
ax = plt.gca()
ax.set_facecolor('w')
plt.show()

__author__ = "Md Tariqul Islam"
__version__ = "1.0"
__maintainer__ = "Tariqul"
__email__ = "tariquldipu@uni-koblenz.de"
__status__ = "Final"
