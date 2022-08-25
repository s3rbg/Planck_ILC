#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 19:45:39 2022

@author: sergio
"""
import numpy as np
from evaluate import evaluate
from astropy.io import fits
import healpy as hp 
from covariance2 import cov
import os

# def covar(maps, template=None):
def covar(maps, template=None, folder='output/operators/', file_name='cov.fits'):
    """
    

    Parameters
    ----------
    maps : array-like
        column format array with the data of all the maps
    template : array-like
        Separation templation, with the same number of pixels as the 
        maps and not repeated indexes in separated regions. 
        If not given, taken all map by default
    """
    file = str(folder)+str(file_name)
    if os.path.exists(file):
        if(input('File found, overwrite? [y/n]: ')) != 'y':
            print('Aborted')
            return
        else:
            os.remove(file)
    template, val = evaluate(template, len(maps))
    C = []
    #Loop over all regions
    for i in val:
        index = np.where(template==i)[0]
        C.append(cov(maps[index]))
    
    h1 = fits.HDUList([fits.PrimaryHDU(C)])
    h1.writeto(file)
    