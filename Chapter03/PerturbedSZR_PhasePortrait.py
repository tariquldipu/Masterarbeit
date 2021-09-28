#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This program plots the Phase Portrait for the Perturbed SZR Model

    Reference: Allen, Robert F., Cassandra Jens, and Theodore J. Wendt. 2014.
   “Perturbations in Epidemiological Models”. Letters in Biomathematics 1 (2), 173-80.
   Link- https://doi.org/10.1080/23737867.2014.11414478.

   Part of MS Thesis at Universität Koblenz-Landau
   Note: this program uses the following libraries-  Numpy, Matplotlib
   Python Version 3.7
"""
# Phase Portrait For Perturbed SZR Model

# importing libraries
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
figure(figsize=(6, 6), dpi=150)


# Parameter values
beta = 0.0095
alpha = 0.005
zeta = 0.0001
N = 1000  #initial population

x = np.arange(0, 800, 1)
y = np.arange(0, 800, 1)
S, Z = np.meshgrid(x, y)

# range of values for Mu, with an increment of 0.005
mu = 0.175

S_dash = - beta*S*Z #SZR model differential equation
Z_dash = zeta*(N - S - Z) + beta*S*Z - alpha*(S**(1 + u))*Z #SZR model differential equation
plt.streamplot(S, Z, S_dash, Z_dash, density=1.1) #phase portrait
plt.title("Perturbed SZR model with mu= %1.3f" %u)
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
