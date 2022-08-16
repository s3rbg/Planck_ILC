#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 15:19:14 2022

@author: sergio
"""
import numpy as np
from astropy.io import fits
from tqdm import tqdm
def cov(maps, mean):
    """
    Computes the covariance matrix
    of the given maps

    Parameters
    ----------
    maps : array
        raw data of the maps, in column format
    mean : array
        data with the mean value for each pixel

    Returns
    -------
    Covariance matrix

    """
    
    n_maps = len(maps[0])
    n_pix = len(maps)
    #Initialize matrix as an array
    C = np.array([[0.]*n_maps]*n_maps)
    # counter = 0
    num = n_maps**2
    #Nested loop over maps
    for i in range(n_maps):
        for j in range(n_maps):
            # counter +=1
            # print('\n\nIteration', counter, 'of', num, '\n')
            suma=0.
            #Loop over pixels
            
            for p in range(n_pix):
                suma += (maps[p, i] - mean[p])*(maps[p, j]-mean[p])
            C[i, j] = suma/n_pix
    return C