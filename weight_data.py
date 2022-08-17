# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:19:59 2022

@author: Sergio
"""
import numpy as np
from tqdm import tqdm
from astropy.io import fits
from save_data import save

def weight_data(data, w, data_raw):
    #Case 1 - full map, straight forward computation
    if len(w.shape)==1:
        data_fin = np.copy(data)
        for i in range(len(w)):
            data_fin[:,i] = data[:,i] * w[i]
            #data ready for storage
    #Case 2 - work with slices
    else:
        #   Initialize final array as a line of 0s
####Note: Remember to erase that line at the end
        print('\n\nWeighing data\n\n')
        data_fin = np.array([[0]*len(w[0])])
        
       
        
        for i in tqdm(range(len(w))):
            data_i = data[i]
            data_aux = np.copy(data_i)
            w_i = w[i]
            for j in range(len(w_i)):
                data_aux[:,j] = data_i[:,j]*w_i[j]
            #slice of data weighted, store in data final
            data_fin = np.concatenate((data_fin, data_aux))
        data_fin = np.delete(data_fin, 0, 0)
        data_fin=np.delete(data_fin, slice(len(data_raw), len(data_fin)), 0)
        map_fin = []
        for i in tqdm(data_fin):
            map_fin.append(np.sum(i))
        h1 = fits.HDUList([fits.PrimaryHDU(data_fin)])
        h2 = fits.HDUList([fits.PrimaryHDU(map_fin)])
        h1.writeto('data/data_w.fits')
        h2.writeto('data/sum_w.fits')