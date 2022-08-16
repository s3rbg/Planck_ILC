# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:52:33 2022

@author: Sergio
"""
import numpy as np
from astropy.io import fits
from tqdm import tqdm
from covariance import cov
import os

def save_cov(data, mean, folder='data/weight/', data_exp='data_exp.fits', 
             file_cov='Cov.fits', n_data=0, n_it=1):
    """
    Computes and saves covariance matrix (file is readed as arrays)

    Parameters
    ----------
    data : array
        data of all maps, in columns (each column is a map)
    mean : array
        array with the mean values of the previous data, in column format
    folder_new: str
        path to save the files
    data_exp: str
        name of the file to save the sliced data
    file_cov: str
        name of the file to save the covariance matrix
    n_data : int, optional
        Amount of data taken in each iteration
    n_it : int, optional
        Number of iterations. The default is 1
        
    n_data is prioritary over n_it

    """
    if not os.path.exists(folder):
        os.mkdir(folder)
    f1 = str(folder)+str(data_exp)
    f2 = str(folder)+str(file_cov)
    
    if os.path.exists(f1) or os.path.exists(f2):
        if input('Files already found. Overwrite? [y/n]: ') != 'y':
            print('aborted')
            return
        if os.path.exists(f1):
            os.remove(f1)
        if os.path.exists(f2):
            os.remove(f2)
            
            
    #If n_data specified, "delete" n_it to avoid future errors
    if n_data != 0:
        n_it = 0
    #If n_data not specified, compute it from n_it
    if n_data == 0:
        n_data = int(np.ceil(len(mean))/n_it)
    
    #Remaining data to make n_it exact
    rem = n_data - (len(mean)%n_data)
    
    #Add lack of data from the beginning to the end
    if rem != 0:
        data = np.concatenate((data, data[0:rem]))
        mean = np.concatenate((mean, mean[0:rem]))
    #Compute n_it if needed
    if n_it == 0:
        n_it = int(len(mean)/n_data)
        
    #Compute C for all the slices of data
    C = []
    data_slc = []
    for i in tqdm(range(n_it)):
        # print('\n\nComputing C '+str(i+1)+' of '+str(n_it))
        slc_dat = data[n_data*i:n_data*(i+1)]
        slc_mean = mean[n_data*i:n_data*(i+1)]
        data_slc.append(slc_dat)
        C.append(cov(slc_dat, slc_mean))
    
    h1 = fits.HDUList([fits.PrimaryHDU(data_slc)])
    h2 = fits.HDUList([fits.PrimaryHDU(C)])
    h1.writeto(f1)
    h2.writeto(f2)