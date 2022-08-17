#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:54:37 2022

@author: sergio
"""
#Dictionary to convert data to kelvin
transform = {'K_CMB': 1, 'uK_CMB': 1e-6}
c = 3e8 #m/s, speed of light
k_b = 1.380649e-23 #J/K, Boltzmann constant
def factor_MJy(frec):
    """
    
    #Conversion factor from MJy/sr to K
    Parameters
    ----------
    frec : float, string
        frecuency, in GHz

    Returns
    -------
    Factor to convert to K

    """

    return 1e-38*c**2/float(frec)**2/2/k_b
    