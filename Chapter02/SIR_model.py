#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Simulation of SIR Moodel with sample data
    Influenza epidemic data in a boys boarding school in the north of England in 1978

    Reference:
            1. Kermack, W. O., & McKendrick, A. G. (1927). A contribution to the mathematical theory of epidemics.
            Proceedings of the royal society of london.
            Series A, Containing papers of a mathematical and physical character, 115(772), 700-721.
            2. SIR Model of Epidemics- Basic Model and Examples, Revised September 22, 2005, University of Rochester
                URL- http://www2.me.rochester.edu/courses/ME406/webexamp5/sir1.pdf
            3. British Medical Journal, March 4 1978, p. 587
                URL- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1603269/pdf/brmedj00115-0064.pdf

   Part of MS Thesis at Universität Koblenz-Landau
   Note: this program uses the following libraries-  Numpy, Matplotlib, Scipy
   Python Version 3.7
"""

# importing libraries
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Just for a pretier plot
plt.style.use('ggplot')

# Parameter values
beta = 0.00218
alpha = 0.441
N = 763  # total population


# Defining Function of the SZR ODE
def model(t, x):
    S = x[0] # Intital Susceptible Population
    I = x[1] # Initial Infected Population
    dsdt = - beta*S*I # Susceptible
    didt = beta*S*I - alpha*I # Infected
    dxdt = [dsdt, didt]
    return dxdt

# Initial Condition. Susceptible= 762, Infected= 01
x0 = [762, 1]

# Time, as in number of days. Total days= 14
t = np.array([0, 14])
tspan = np.linspace(t[0], t[1], 15)

# Calculating numerical solution of the given ODEs
x = solve_ivp(model, t, x0, t_eval=tspan)

time = x.t
susceptible = x.y[0];
infected = x.y[1];
recovered = (N - susceptible - infected);

# Plot
plt.plot(time, susceptible, 'b-', label="Susceptible") # Susceptible Population Graph
plt.plot(time, infected, 'r--', label="Infected") # Infected Population Graph
plt.plot(time, recovered, 'g:', label="Recovered") # Recovered Population Graph
plt.ylabel('Population')
plt.xlabel('Time (Days)')
plt.legend(loc='best')
plt.title('SIR Model')
plt.grid(True)
ax = plt.gca()
ax.set_facecolor('w')
plt.show()

__author__ = "Md Tariqul Islam"
__version__ = "1.0"
__maintainer__ = "Tariqul"
__email__ = "tariquldipu@uni-koblenz.de"
__status__ = "Final"
