# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:01:58 2021

@author: Lea
"""
import numpy as np
from dataclasses import dataclass
import pandas as pd

@dataclass
class Calculations:
    '''Class for retrieving the properties, calculating IMFP and probing depth and generating a dataset in a dataframe.'''
    df = 0
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
    #compound = 0
    
    def __init__(self, compound):
        self.df = 0
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
        #self.compound = compound

    
    def get_properties(self, compound):
        """
        Retrieves properties that are needed for the calculation from the dataset for the input compound and stores in attribute.
        """
        data = pd.read_csv(r'./data/tblIMFPdata.csv', delimiter = ';', dtype={'Density': float, 'Atomic wght': float, 'valel s+p,n+1': float, 'Energy gap 300 K': float})
        data = data.fillna(0)
        row_index = data[data["Name"] == compound].index
        self.density = data.iloc[row_index ,4]
        self.density = self.density.iloc[0]
        self.molecular_weight = data.iloc[row_index ,5]
        self.molecular_weight = self.molecular_weight.iloc[0]
        self.number_VE = data.iloc[row_index ,7] + data.iloc[row_index ,9] + data.iloc[row_index ,10]
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
