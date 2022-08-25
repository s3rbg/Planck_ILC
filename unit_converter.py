#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:54:37 2022

@author: sergio
"""
import numpy as np
#Dictionary to convert data to kelvin
transform = {'K_CMB': 1, 'uK_CMB': 1e-6}
c = 3e8 #m/s, speed of light
k_b = 1.380649e-23 #J/K, Boltzmann constant
h = 6.62607015e-34 #J s
def arcmin2rad(ang):
    return ang/60/180*np.pi

def factor_MJy(frec, ang):
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
    # data *= 1e-20 #Convert data to W m-2 Hz-1 sr-1
    # frec *= 1e9 #Convert frecuency to Hz
    # log_term = (np.pi*arcmin2rad(ang)**2*h*frec**3)/(2*data*c**2)
    
    # return (h*frec)/(k_b*(1+np.log(log_term)))
    return 1e-38*(2*c**2*np.log(2))/(k_b*np.pi*float(frec)**2*arcmin2rad(ang)**2)
