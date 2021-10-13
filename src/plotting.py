# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:53:46 2021

@author: Lea
"""

import matplotlib.pyplot as plt
from calculations import Calculations
from dataclasses import dataclass
import pandas as pd
import os



@dataclass
class Plotting:

    df = 0
    fig, ax = plt.subplots(figsize=(10, 5))
    one = 0
    element = 0

    def __init__(self, element):
        self.df = 0
        self.one = Calculations(element)
        self.element = element


    def gen_dataset(self, min_e, max_e):
        """Generates and returns dataset with calculated IMFP and probing depth for given energy range."""
        self.one.calc_constants(self.element)
        list_e = []
        list_imfp = []
        list_pd = []
        
        while min_e < max_e+1:
            self.one.calc_imfp_probdepth(min_e)
            list_e.append(min_e)
            list_imfp.append(self.one.lam)
            list_pd.append(self.one.prob_depth)
            min_e += 1
            
        self.df = pd.DataFrame(list(zip(list_e, list_imfp, list_pd)))
        self.df.columns = pd.MultiIndex.from_arrays([["Properties used for calculation:","",""],
                                                     ["Density / g/cm3", self.one.density, ""],
                                                     ["Atomic mass", self.one.molecular_weight, ""],
                                                     ["Band gap / eV", self.one.band_gap_E,""],
                                                     ["Valence electrons", self.one.number_VE, ""],
                                                     ["Electron energy/eV", "IMFP / nm", "Probing depth / nm"]])
                   
        if not os.path.exists("results") :
            os.mkdir("results")                                 
        self.df.to_csv(os.path.join("results","IMFP_"+self.element+"_data.csv"), sep = ",")
    
    def plot_imfp(self, min_e, max_e):
        self.gen_dataset(min_e, max_e)
        self.ax.plot(self.df.iloc[:,0], self.df.iloc[:,1], 
                     label="IMFP " +self.element, color='#44AA99')
        self.ax.plot(self.df.iloc[:,0], self.df.iloc[:,2], 
                     label="Probing depth " +self.element, color='#117733')
        self.ax.set_xlabel('Kinetic energy / eV')
        self.ax.set_ylabel('Path length / nm')
        self.ax.legend()
        self.ax.set_title("IMFP and Probing depth")
        plt.savefig(os.path.join("results","IMFP_"+self.element+".png"), dpi=600)
        plt.show()
        
    