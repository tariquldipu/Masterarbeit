#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This program plots the Phase Portrait for the Modified SEZQR Model

   Part of MS Thesis at Universität Koblenz-Landau
   Note: this program uses the following libraries-  Numpy, Matplotlib
   Python Version 3.7
"""
# Phase Portrait For Modified SEZQR Model

# importing libraries
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
figure(figsize=(6, 6), dpi=150)


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

x = np.arange(0, 800, 1)
y = np.arange(0, 800, 1)
S, Z = np.meshgrid(x, y)
p = np.arange(0, 800, 1)
q = np.arange(0, 800, 1)
E, Q = np.meshgrid(p, q)

# range of values for Mu, with an increment of 0.005
mu = 0.175

S_dash = - beta*S*Z #SEZQR model differential equation- Susceptible
#E_dash = beta*S*Z - (rho + kappa)*E # Exposed
Z_dash = rho*E + zeta*(N - S - E - Z - Q) - sigma*S*Z - alpha*(S**(1 + mu))*Z + omega*Q #SEZQR model differential equation- Zombie
#Q_dash = kappa*E + sigma*S*Z - gamma*Q - omega*Q # Quarantined
plt.streamplot(S, Z, S_dash, Z_dash, density=1.1) #phase portrait
plt.title("Modified SEZQR Model With Perturbation")
plt.axis("scaled")
plt.draw()
plt.xlabel("Humans")
plt.ylabel("Zombies")
ax = plt.gca()
ax.set_facecolor('w')

__author__ = "Md Tariqul Islam"
__version__ = "1.0"
__maintainer__ = "Tariqul"
__email__ = "tariquldipu@uni-koblenz.de"
__status__ = "Final"
