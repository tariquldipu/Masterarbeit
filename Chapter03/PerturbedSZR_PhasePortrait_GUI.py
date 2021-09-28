#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This program attempts to create a simple interactive window to draw the phase portrait of SZR Model

   Perturbed SZR Model, Phase Portrait Generator

   Reference: Allen, Robert F., Cassandra Jens, and Theodore J. Wendt. 2014.
   “Perturbations in Epidemiological Models”. Letters in Biomathematics 1 (2), 173-80.
   Link- https://doi.org/10.1080/23737867.2014.11414478.

   Part of MS Thesis at Universität Koblenz-Landau

   Instructions: After running the code, please input the required values in the text
   fields of the newly generated window and then click on 'Generate Phase Portrait'
   to create and show the drawn phase portrait on the window. You can change or update the values
   to draw new portraits. You can save the image separately from the interactive window.

   Please only input numerical values in the given fields. Otherwise, the program will fail to run.
   Please only input numerical values for the fields- Alpha, Beta, Zeta, Mu, within the range between 0 and 1.
   Please only input integer value for the field Population N.

   Note: this program uses the following libraries- Tkinter, Numpy, Scipy, Matplotlib
   Python Version 3.7
"""

# importing libraries
from tkinter import *
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


# defining class
class MyWindow:
    def __init__(self, win):
        # header text and equation text with their positions in the window
        lble1=Label(window, text="Generate Phase Portrait of the SZR Model", fg='black', font=("Helvetica", 16))
        lble1.place(x=300, y=20)
        lble2=Label(window, text="S\' = -\u03b2SZ")
        lble2.place(x=650, y=80)
        lble3=Label(window, text="Z\' = \u03b6(N - S - Z) + \u03b2SZ - \u03b1S\u207D\u00b9 \u207a \u1d58\u207eZ")
        lble3.place(x=650, y=100)
        lble4=Label(window, text="Differential Equation", fg='black', font=("Helvetica", 14))
        lble4.place(x=650, y=60)

        # input field titles
        self.lbl1=Label(win, text='Alpha '+ u"\u03b1")
        self.lbl2=Label(win, text='Beta '+ u"\u03b2")
        self.lbl3=Label(win, text='Zeta '+ u"\u03b6")
        self.lbl4=Label(win, text='Mu ' + u"\u03bc")
        self.lbl5=Label(win, text='Population N')

        # input fields
        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        self.t3=Entry(bd=3)
        self.t4=Entry(bd=3)
        self.t5=Entry(bd=3)

        # setting up titles and input fields positions
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)
        self.lbl4.place(x=100, y=200)
        self.t4.place(x=200, y=200)
        self.lbl5.place(x=100, y=250)
        self.t5.place(x=200, y=250)

        # setting up button
        self.b1=Button(window, text=' Generate Phase Portrait ', command=self.plot)
        self.b1.place(x=100, y=300)

    # defining function for the main calculation
    def plot(self):
        # getting paramaeter values
        alpha = float(self.t1.get())
        beta = float(self.t2.get())
        zeta = float(self.t3.get())
        mu = float(self.t4.get())
        N = int(self.t5.get())

        # equation set up
        x = np.arange(0, 800, 1)
        y = np.arange(0, 800, 1)
        S, Z = np.meshgrid(x, y)
        S_dash = -beta*S*Z
        Z_dash = zeta*(N - S - Z) + beta*S*Z - alpha*(S**(1 + mu))*Z

        # drawing figure
        fig = Figure(figsize=(5,3.5), dpi=100)
        a = fig.add_subplot(111)
        a.clear()
        title = "Phase Portrait with " + u"\u03bc" + "= "
        a.set_title(title + str(mu))
        a.set_xlabel("Humans")
        a.set_ylabel("Zombies")
        a.streamplot(S, Z, S_dash, Z_dash, density=1.0)

        # figure on tkinter canvas and navigation toolbar
        myCanvas = FigureCanvasTkAgg(fig, window)
        toolbar = NavigationToolbar2Tk(myCanvas, window)
        myCanvas.get_tk_widget().place(x=200, y=330)
        myCanvas.draw_idle()
        toolbar.place(x=350, y=700)
        toolbar.update()

# loading tkinter
window=Tk()
mywin=MyWindow(window)
window.title('Phase Portrait of Perturbed SZR Model') # tkinter window title
window.geometry("900x800+10+20") # tkinter window dimension
window.mainloop()

__author__ = "Md Tariqul Islam"
__version__ = "1.0.1"
__maintainer__ = "Tariqul"
__email__ = "tariquldipu@uni-koblenz.de"
__status__ = "Production"
