#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This simple program tries to solve the ODE of the Perturbed SZR model
    and create a numerical solution.
    After that, this program draws the solution graph for only the Zombie Population with the gradual
    increase of perturbation parameter.
    This simple graph helps us to understand the actual scenario of the zombie population
    from the Perturbed SZR model with respect to the perturbation parameter.

   Part of MS Thesis at Universität Koblenz-Landau
   Note: this program uses the following libraries-  Numpy, Matplotlib, Scipy
   Python Version 3.7
"""

# Perturbed SZR Model

# importing libraries
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
figure(figsize=(6, 6), dpi=150)

# For a nice looking plot
plt.style.use('ggplot')

# Parameter values
beta = 0.0095
alpha = 0.005
zeta = 0.0001
N = 1000  # initial population

# Defining Function of the SZR ODE
def model(t, x):
    S = x[0] # Intital Susceptible Population
    Z = x[1] # Zombies
    dsdt = - beta*S*Z # Susceptible
    dzdt = zeta*(N - S - Z) + beta*S*Z - alpha*(S**(1 + mu))*Z # Zombies
    dxdt = [dsdt, dzdt]
    return dxdt

# Initial Condition. Susceptible= 800, Zombie= 200
x0 = [800, 200]

# Time, as in number of days. Total days= 1000
t = np.array([0, 10])
tspan = np.linspace(t[0], t[1], 1000)


# Calcuclate zombie population for different values of Mu
mu = 0.0
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie01 = x.y[1]

mu = 0.05
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie02 = x.y[1]

mu = 0.1
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie03 = x.y[1]

mu = 0.15
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie04 = x.y[1]

mu = 0.2
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie05 = x.y[1]

mu = 0.25
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie06 = x.y[1]

time = x.t
# Plot
plt.plot(time, zombie01, 'r--', label="Mu=0.0")
plt.plot(time, zombie02, 'b:', label="Mu=0.05")
plt.plot(time, zombie03, 'c-.', label="Mu=0.1")
plt.plot(time, zombie04, 'g-', label="Mu=0.15")
plt.plot(time, zombie05, 'y-', label="Mu=0.2")
#plt.plot(time, zombie06, 'k', label="Mu=0.25")

plt.title('Zombie Population For Different Mu')
plt.ylabel('Zombie Population')
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
