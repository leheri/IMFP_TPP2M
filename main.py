# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:23:12 2021

@author: Lea
"""

# import packages
from plotting import Plotting

# asking user for the wished element
element = input("Which compound / element should I plot for you? ")

# Asking for energy range e
min_e = float(input("Minimal electron energy / eV: "))
max_e = float(input("Maximal electron energy / eV: "))

# generating data set, plotting and saving files
one = Plotting(element)
one.plot_imfp(min_e, max_e)

