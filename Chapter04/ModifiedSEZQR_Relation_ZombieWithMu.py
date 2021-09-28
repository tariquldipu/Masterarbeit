#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modified SEZQR Model

"""This simple program tries to show a relation between the number of zombies and the perturbation value Mu.
    This program is calculated at the point t = 1000 days.
    It shows that, at t = 1000 days, as the value of the pertubation parameter Mu increases, the number of total
    zombies decreases. Thus, establishing the fact that the perturbation parameter has a direct impact on the
    zombie population.

   Part of MS Thesis at Universität Koblenz-Landau
   Note: this program uses the following libraries-  Numpy, Matplotlib, Scipy
   Python Version 3.7
"""

# importing libraries
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
figure(figsize=(6, 6), dpi=150)
import warnings
warnings.filterwarnings("ignore")

# Generating range of values for Mu, from 0.0 upto 0.5, with an increment of 0.025
mu = np.arange(0.0, 0.5, 0.025)

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

def model(t, x):
    S = x[0] # Intital Susceptible Population
    E = x[1] # exposed
    Z = x[2] # zombies
    Q = x[3] # quarentined
    dsdt = - beta*S*Z # Susceptible
    dedt = beta*S*Z - (rho + kappa)*E # Exposed
    dzdt = rho*E + zeta*(N - S - E - Z - Q) - sigma*S*Z - alpha*(S**(1 + value))*Z + omega*Q # Zombies
    dqdt = kappa*E + sigma*S*Z - gamma*Q - omega*Q # Quarantined
    dxdt = [dsdt, dedt, dzdt, dqdt]
    return dxdt

# Initial Condition. Susceptible= 700, Exposed= 100, Zombie= 130, Quarantined = 70
x0 = [700, 100, 130, 70]

# Time, as in number of days. Total days= 1000
t = np.array([0, 1000])
tspan = np.linspace(t[0], t[1], 1000)

i = 0;

# empty lists
zombie_new = []
recovered_new = []

for value in mu:
    x_new = solve_ivp(model, t, x0, t_eval=tspan)
    zombie = x_new.y[2];
    zombie_new.append(zombie[999])
    #susceptible = x_new.y[0];
    #recovered_new.append((N - susceptible[999] - zombie[999]))

# Drawing Scatter Plot at t = 1000 days position
# Change of zombie numbers with the increase of Mu Values
# When the number of zombies reaches 0 at t= 1000 days, the model reaches stability at that Mu value
plt.plot(mu, zombie_new, 'o', color='black');
#plt.plot(mu, recovered_new, 'o', color='blue');
plt.ylabel('Zombie Population')
plt.xlabel('Mu Values')
plt.title("Decrease of Zombie Population With The Increase of Mu Values, at t= 1000 days")
ax = plt.gca()
ax.set_facecolor('w')
plt.show
