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

# Classical SIR Model- PHASE PORTRAIT

# importing libraries

import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
from matplotlib.pyplot import figure
figure(figsize=(7, 7), dpi=80)

# Parameter values
beta = 0.00218
alpha = 0.441
N = 763  # total population

x = np.arange(0, 800, 1)
y = np.arange(0, 800, 1)
S, I = np.meshgrid(x, y)

S_dash = - beta*S*I # Susceptible
I_dash = beta*S*I - alpha*I #Infected

plt.streamplot(S, I, S_dash, I_dash, density=1.0, color='r')
plt.title("SIR model- Phase Portrait")
plt.axis("scaled")
ax = plt.gca()
ax.set_facecolor('w')
ax.set_xlabel("Humans")
ax.set_ylabel("Infected")
plt.show()

__author__ = "Md Tariqul Islam"
__version__ = "1.0"
__maintainer__ = "Tariqul"
__email__ = "tariquldipu@uni-koblenz.de"
__status__ = "Final"
