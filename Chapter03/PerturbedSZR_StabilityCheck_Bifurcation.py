#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This simple program tries to check the stability of the SZR model,
    for the different values of Mu (perturbation parameter), starting from 0, with an increment of 0.005.
    The program will continue to run until it finds a optimal value of Mu,
    for which the SZR model reaches stability.
    As soon as the program finds the value of Mu for which the SZR model
    reaches stability, it will stop then and there and draw a simplified bifurcation diagram.

    Reference: Allen, Robert F., Cassandra Jens, and Theodore J. Wendt. 2014.
   “Perturbations in Epidemiological Models”. Letters in Biomathematics 1 (2), 173-80.
   Link- https://doi.org/10.1080/23737867.2014.11414478.

   Part of MS Thesis at Universität Koblenz-Landau
   Note: this program uses the following libraries-  Numpy, Matplotlib
   Python Version 3.7
"""

# importing libraries
import numpy as np
from matplotlib import pyplot as plt


# Parameter values
beta = 0.0095
alpha = 0.005
zeta = 0.0001
N = 1000  #initial population

x = np.arange(0, 800, 1)
y = np.arange(0, 800, 1)
S, Z = np.meshgrid(x, y)

# range of values for Mu, with an increment of 0.005
mu_list = np.arange(0.0, 1.0, 0.005)

for u in mu_list:
    S_dash = - beta*S*Z #SZR model differential equation
    Z_dash = zeta*(N - S - Z) + beta*S*Z - alpha*(S**(1 + u))*Z #SZR model differential equation
    plt.streamplot(S, Z, S_dash, Z_dash, density=1.5) #phase portrait
    plt.title("Perturbed SZR model with mu= %1.3f" %u)
    plt.axis("scaled")
    #plt.figure(figsize=(8,8));
    plt.draw()
    plt.xlabel("Humans")
    plt.ylabel("Zombies")
    plt.pause(0.0001)
    plt.clf()

    if (u > (((np.log((beta*N - zeta)/(alpha)))/(np.log(N))) - 1)):  #checking for stable value point
        break


print("##########################################")
print("So the model reaches stability at Mu= ", str(u))
print("##########################################")
print("")
print("")
print("The bifurcation diagram for the SZR model >>>>>")

x = np.array(range(2,1000))
y = ((np.log((beta*x - zeta)/(alpha)))/(np.log(x))) - 1
# draw bifurcation diagram
plt.plot(x,y)
plt.ylim([0, 0.4])
plt.xlim([0, 600])
plt.yticks(np.arange(0, 0.4, 0.1))
plt.xticks(np.arange(0, 600, 100))
plt.xlabel("Population N")
plt.ylabel("Mu " + u"\u03bc")
plt.text(400, 0.12, "Stable",
        fontsize= 14,
        color= 'green')
plt.text(400, 0.07, "Unstable",
        fontsize= 14,
        color= 'red')
plt.text(600, -0.02, "N")
plt.text(-20, 0.4, u"\u03bc")
plt.annotate(r"$ \frac{\ln(\frac{\beta N - \zeta}{\alpha})}{\ln N} - 1$", xy=(100, 0.15), xytext=(200, 0.2),
            arrowprops=dict(facecolor='black', shrink=1))# theorem 1 condition
plt.show()


__author__ = "Md Tariqul Islam"
__version__ = "1.0"
__maintainer__ = "Tariqul"
__email__ = "tariquldipu@uni-koblenz.de"
__status__ = "Final"
