# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:01:58 2021

@author: USER
"""
import numpy as np
from dataclasses import dataclass
import pandas as pd

@dataclass
class Calculations:
    '''Class for retrieving the properties, calculating IMFP and probing depth and generating a dataset in a dataframe.'''
    df = pd.DataFrame()
    density =0.0
    molecular_weight =0.0
    number_VE=0.0
    band_gap_E=0.0
    plasmon_energy=0.0
    beta=0.0
    gamma=0.0
    c=0.0
    d=0.0
    lam = 0.0
    prob_depth = 0.0
    df=0
    
    def __init__(self):
        self.df = pd.DataFrame()
        self.density =0.0
        self.molecular_weight =0.0
        self.number_VE=0.0
        self.band_gap_E=0.0
        self.plasmon_energy=0.0
        self.beta=0.0
        self.gamma=0.0
        self.c=0.0
        self.d=0.0
        self.lam = 0.0
        self.prob_depth = 0.0
        self.df=0

    
    def get_properties(self, compound):
        """
        Retrieves properties that are needed for the calculation from the dataset for the input compound and stores in attribute.
        """
        data = pd.read_csv(r'./TPP2-data/tblIMFPdata.csv', delimiter = ';', dtype={'Density': float, 'Atomic wght': float, 'valel s+p,n+1': float, 'Energy gap 300 K': float})
        row_index = data[data["Name"] == compound].index
        self.density = data.iloc[row_index ,4]
        self.density = self.density.iloc[0]
        self.molecular_weight = data.iloc[row_index ,5]
        self.molecular_weight = self.molecular_weight.iloc[0]
        self.number_VE = data.iloc[row_index ,7]
        self.number_VE = self.number_VE.iloc[0]
        self.band_gap_E = data.iloc[row_index, 11]
        self.band_gap_E = self.band_gap_E.iloc[0]

    
    def calc_constants(self, compound):
        """Calculates the constants from the properties of the element and stores in the attributes."""
        self.get_properties(compound) 
        self.plasmon_energy = 28.8 * (((self.number_VE * self.density) / self.molecular_weight) ** (0.5))
        self.beta = -0.10+0.944*((self.plasmon_energy**2+self.band_gap_E**2)**(-0.5))+0.069*self.density**(0.1)
        u = self.number_VE*self.density/self.molecular_weight
        self.gamma = 0.191*self.density**(-0.5)
        self.c = 1.97 - (0.91 * u)
        self.d = 53.4-20.8*u
        
        
    def calc_imfp_probdepth(self, x):
        """
        Calculates the IMFP by the non-relativistic TPP-2M formula in nm.
        """
        self.lam = (x / (self.plasmon_energy**2*((self.beta*np.log(self.gamma*x))-(self.c/x) + (self.d/x**2)))/10)
        self.prob_depth = 3*self.lam


    def gen_dataset(self, element, min_e, max_e):
        """Generates and returns dataset with calculated IMFP and probing depth for given energy range."""

        self.calc_constants(element)
        list_e = []
        list_imfp = []
        list_pd = []
        
        while min_e < max_e+1:
            self.calc_imfp_probdepth(min_e)
            list_e.append(min_e)
            list_imfp.append(self.lam)
            list_pd.append(self.prob_depth)
            min_e += 1
            
        self.df = pd.DataFrame(list(zip(list_e, list_imfp, list_pd)), columns = ["Electron energy/eV", "IMFP / nm", "Probing depth / nm"])
        return self.df
        
    