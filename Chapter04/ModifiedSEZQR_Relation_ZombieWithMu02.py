#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This simple program tries to solve the ODE of the Modified SEZQR model with perturbation
    and create a numerical solution.
    After that, this program draws the solution graph for only the Zombie Population with the gradual 
    increase of perturbation parameter.
    This simple graph helps us to understand the actual scenario of the zombie population
    from the modified SEZQR model with respect to the perturbation parameter.

   Part of MS Thesis at Universität Koblenz-Landau
   Note: this program uses the following libraries-  Numpy, Matplotlib, Scipy
   Python Version 3.7
"""

# MODIFIED SEZQR MODEL

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


# Defining Function of the SEZQR ODE
def model(t, x):
    S = x[0] # Intital Susceptible Population
    E = x[1] # exposed
    Z = x[2] # zombies
    Q = x[3] # quarentined
    dsdt = - beta*S*Z # Susceptible
    dedt = beta*S*Z - (rho + kappa)*E # Exposed
    dzdt = rho*E + zeta*(N - S - E - Z - Q) - sigma*S*Z - alpha*(S**(1 + mu))*Z + omega*Q # Zombies
    dqdt = kappa*E + sigma*S*Z - gamma*Q - omega*Q # Quarantined
    dxdt = [dsdt, dedt, dzdt, dqdt]
    return dxdt

# Initial Condition. Susceptible= 700, Exposed= 100, Zombie= 130, Quarantined = 70
x0 = [700, 100, 130, 70]

# Time, as in number of days. Total days= 1000
t = np.array([0, 1000])
tspan = np.linspace(t[0], t[1], 10001)

# Calcuclate zombie population for different values of Mu
mu = 0.0
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie01 = x.y[2]

mu = 0.05
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie02 = x.y[2]

mu = 0.1
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie03 = x.y[2]

mu = 0.15
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie04 = x.y[2]

mu = 0.2
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie05 = x.y[2]

mu = 0.25
x = solve_ivp(model, t, x0, t_eval=tspan)
zombie06 = x.y[2]

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
