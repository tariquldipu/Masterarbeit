#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This program plots the bifurcation diagram for the SEZQR Model

    Reference: Allen, Robert F., Cassandra Jens, and Theodore J. Wendt. 2014.
   “Perturbations in Epidemiological Models”. Letters in Biomathematics 1 (2), 173-80.
   Link- https://doi.org/10.1080/23737867.2014.11414478.

   Part of MS Thesis at Universität Koblenz-Landau
   Note: this program uses the following libraries-  Numpy, Matplotlib
   Python Version 3.7
"""
# Bifurcation Diagram For SEZQR Model

# SEZQR MODEL

# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(figsize=(6, 6), dpi=150)


beta = 0.0095
alpha = 0.005
zeta = 0.0001
rho = 0.005
kappa = 0.001
sigma = 0.001
gamma = 0.0001
omega = 0.009
N = 1000


# Create the vectors X and Y
x = np.array(range(2,1000))
temp03 = - alpha*gamma*(rho + kappa)
temp04 = (rho+kappa)*((zeta*sigma)+gamma*(zeta+sigma))
y = (np.log( (beta*x*(zeta*kappa + gamma*(zeta - rho)) + temp04) / (temp03))/(np.log(x))) -1



# Modoified SEZQR
temp01 = ((zeta-rho)*(gamma+omega)+kappa*(zeta-omega))
temp02 = (rho+kappa)*(sigma*x*(zeta - omega) + (gamma+omega)*(zeta + sigma*x))
z = ((np.log((beta*x*temp01 + temp02 )/(-alpha*(gamma+omega)*(rho+kappa))))/(np.log(x))) - 1


# Create the plot
plt.plot(x,y, label='SEZQR')
plt.plot(x,z, label='Modified SEZQR')
plt.ylim([0, 0.4])
plt.xlim([0, 1000])
plt.yticks(np.arange(0, 0.4, 0.1))
plt.xticks(np.arange(0, 1000, 100))
plt.xlabel("Population N")
plt.ylabel("Mu " + u"\u03bc")
plt.legend(loc='best')

plt.text(1000, -0.02, "N")
plt.text(980, -0.004, ">")
#plt.text(0, 0.4, ">")
plt.text(-20, 0.4, u"\u03bc")

#plt.text(600, 0.05, "Stable", fontsize= 14, color= 'green')
#plt.text(600, 0.005, "Unstable", fontsize= 14, color= 'red')


# Show the plot
plt.title("Bifurcation Diagram Comparison")
plt.show()


__author__ = "Md Tariqul Islam"
__version__ = "1.0"
__maintainer__ = "Tariqul"
__email__ = "tariquldipu@uni-koblenz.de"
__status__ = "Final"
