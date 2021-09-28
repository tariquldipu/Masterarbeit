#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This simple program tries to solve the ODE of the Perturbed SZR model and create a numerical solution.
    After that, this program draws the solution graph for the Susceptible, Zombie and Recovered
    Population. This simple graph helps us to understand the actual scenario of the population
    from the SZR model after a certain number of days. We can change the value of the Perturbation
    Parameter Mu to investigate the change of behaviour and stabality of the SZR model.

    Reference: Allen, Robert F., Cassandra Jens, and Theodore J. Wendt. 2014.
   “Perturbations in Epidemiological Models”. Letters in Biomathematics 1 (2), 173-80.
   Link- https://doi.org/10.1080/23737867.2014.11414478.

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

# For a nice looking plot
plt.style.use('ggplot')

# Parameter values
beta = 0.0095
alpha = 0.005
zeta = 0.0001
N = 1000  # initial population

# Perturbation Parameter Mu, change this value to see different results
u = 0.175

# Defining Function of the SZR ODE
def model(t, x):
    S = x[0] # Intital Susceptible Population
    Z = x[1] # Zombies
    dsdt = - beta*S*Z # Susceptible
    dzdt = zeta*(N - S - Z) + beta*S*Z - alpha*(S**(1 + u))*Z # Zombies
    dxdt = [dsdt, dzdt]
    return dxdt

# Initial Condition. Susceptible= 800, Zombie= 200
x0 = [800, 200]

# Time, as in number of days. Total days= 1000
t = np.array([0, 1000])
tspan = np.linspace(t[0], t[1], 1001)

# Calculating numerical solution of the given ODEs
x = solve_ivp(model, t, x0, t_eval=tspan)

time = x.t
susceptible = x.y[0];
zombie = x.y[1];
recovered = (N - susceptible - zombie);

# Plot
plt.plot(time, susceptible, 'b-', label="Susceptible") # Susceptible Population Graph
plt.plot(time, zombie, 'r--', label="Zombie") # Zombie Population Graph
plt.plot(time, recovered, 'g:', label="Removed") # Recovered Population Graph
plt.ylabel('Population')
plt.xlabel('Time (Days)')
plt.title('Perturbed SZR Model for t = 1000 days')
plt.legend(loc='best')
ax = plt.gca()
ax.set_facecolor('w')
plt.show()

__author__ = "Md Tariqul Islam"
__version__ = "1.0"
__maintainer__ = "Tariqul"
__email__ = "tariquldipu@uni-koblenz.de"
__status__ = "Final"
