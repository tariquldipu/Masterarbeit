#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This simple program tries to solve the ODE of the Modified SEZQR model with perturbation and create a numerical solution.
    After that, this program draws the solution graph for the Susceptible, Exposed, Zombie, Quarantined and Removed
    Population. This simple graph helps us to understand the actual scenario of the population
    from the modified SEZQR model after a certain number of days. We can change the value of the Perturbation
    Parameter Mu to investigate the change of behaviour and stabality of the SZR model.

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

# Perturbation Parameter Mu, change this value to see different results
mu = 0.175

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

# Calculating numerical solution of the given ODEs
x = solve_ivp(model, t, x0, t_eval=tspan)

time = x.t
susceptible = x.y[0];
exposed = x.y[1];
zombie = x.y[2]
quarantined  = x.y[3]
removed = (N - susceptible - exposed - zombie - quarantined)

# Plot
plt.plot(time, susceptible, 'b-', label="Susceptible") # Susceptible Population Graph
plt.plot(time, zombie, 'r--', label="Zombie") # Zombie Population Graph
plt.plot(time, removed, 'g-.', label="Removed") # Recovered Population Graph
plt.plot(time, exposed, 'k', label="Exposed") # Exposed Population graph
plt.plot(time, quarantined , 'm:', label="Quarantined")
plt.title('Modified SEZQR Model for t = 1000 days')
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
