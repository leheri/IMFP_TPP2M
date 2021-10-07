# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:23:12 2021

@author: USER
"""

# import packages
import matplotlib.pyplot as plt
import os
from calculations import Calculations

# asking user for the wished element
element = input("Which compound / element should I plot for you? ")
#element2 = input("Which compound / element should I plot for you? ")


# Asking for energy range e
min_e = float(input("Minimal electron energy / eV: "))
max_e = float(input("Maximal electron energy / eV: "))

# generating data set
one = Calculations()
result = one.gen_dataset(element, min_e, max_e)
#sio2 = Calculations()
#result2 = sio2.gen_dataset(element2, min_e, max_e)

# plotting
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(result.iloc[:,0], result.iloc[:,1], label="IMFP " +element, color='#44AA99')
ax.plot(result.iloc[:,0], result.iloc[:,2], label="probing depth " +element, color= '#117733')
#ax.plot(result2.iloc[:,0], result2.iloc[:,1], label="IMFP "+element2, color='#882255')
#ax.plot(result2.iloc[:,0], result2.iloc[:,2], label="probing depth "+element2, color= '#CC6677')

ax.set_xlabel('Electron energy / eV')
ax.set_ylabel('Path length / nm')
ax.legend()
ax.set_title("IMFP and Probing depth of " + element)

# make results folder if it does not exist
if not os.path.exists("results") :
    os.mkdir("results")

# saving figure and dataset
plt.savefig(os.path.join("results",element+".png"), dpi=600)
result.to_csv(os.path.join("results",element+"_data.csv"), sep = ",")