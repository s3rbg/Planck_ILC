#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 11:30:18 2022

@author: sergio
"""
import numpy as np
from tqdm import tqdm 
from astropy.io import fits
from healpy.fitsfunc import read_map 
import os
from unit_converter import transform, factor_MJy

def save(data_origin,frecs, direc='./data/', data_file='data.fits', data_file_mean='mean.fits'):
    """
    Given several .fits data files, they are
    put together in a txt file, as well as its mean

    Parameters
    ----------
    data_origin: List
        paths where all the data files are stored
    
    direc: str. Default is './data/'
        Folder where the data is going to be stored
    
    data_file: str. Default is 'data.fits'
        Name of the file where all the data is going to be stored
    
    data_mean: str. Default is 'mean.fits'
        Name of the file where the data means are going to be stored
    
    """  
    # create folder if needed
    if not os.path.exists(direc):
        os.mkdir(direc)
    f1 = str(direc)+str(data_file)
    f2 = str(direc)+str(data_file_mean)
    # print(f1)
    # print(os.path.exists(direc))
    # print(os.path.exists(f1))
    if os.path.exists(f1) or os.path.exists(f2):
        if input('Files already found. Overwrite? [y/n]: ') != 'y':
            print('aborted')
            return
        if os.path.exists(f1):
            os.remove(f1)
        if os.path.exists(f2):
            os.remove(f2)
    #Check if files already exists, if so, ask for permission to overwrite
    
    
    #First, read the files
    
    #Empty lists to add the data and the units
    data = []
    #Go down the raw data files
    for j, i in enumerate(data_origin):
        #Check units
        hdr = fits.open(i)[1].header
        units = hdr['TUNIT1']
        if units == 'MJy/sr':
            factor = factor_MJy(frecs[j], hdr['BEAMSIZE']/60)
        else:
            factor = transform[units]
        #Read the file, transform to K and add to data list
        data.append(read_map(i, dtype=np.float64)*factor)
    #Convert to array for treatment
    data = np.array(data).T
    
    #Compute mean
    mean = []
    for i in tqdm(data):
        mean.append(np.mean(i))
    mean = np.array(mean)
    h1 = fits.HDUList([fits.PrimaryHDU(data)])
    h2 = fits.HDUList([fits.PrimaryHDU(mean)])
    h1.writeto(f1)
    h2.writeto(f2)
        
    
            
    # return data
        
    
    
    
    