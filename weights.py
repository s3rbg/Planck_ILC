#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:01:07 2022

@author: sergio
"""
import numpy as np
from astropy.io import fits
from tqdm import tqdm
import os

def get_weights(C):
    w = []
    C_m = np.asmatrix(C)
    C_inv = np.linalg.inv(C_m)
    den = np.sum(C_inv)
    for i in C_inv:
        w.append(np.sum(i)/den)
    return np.array(w)   
        
def save_weights(C, folder='data/weight2/', file = 'w.fits'):
    
    if not os.path.exists(folder):
        os.mkdir(folder)
    f1 = str(folder)+str(file)
    
    
    if os.path.exists(f1):
        if input('Files already found. Overwrite? [y/n]: ') != 'y':
            print('aborted')
            return
        if os.path.exists(f1):
            os.remove(f1)
    w = []
    
    for i in tqdm(C):
        aux = []
        i = np.linalg.inv(np.matrix(i))
        den = np.sum(i)
        for j in i:
            aux.append(np.sum(j)/den)
        w.append(np.array(aux))
    h1 = fits.HDUList([fits.PrimaryHDU(w)])
    h1.writeto(f1)
# def test():
#     C = np.genfromtxt('data/cov.txt', skip_header=2)
#     w = get_weights(C)
#     data = fits.getdata('data/data.fits')
#     # print(data[0, 0])
#     # print(data[0, 0]*w[0])
#     data[:,0]*=w[0]
#     data[:,1]*=w[1]
#     data[:,2]*=w[2]
    
#     mean = []
#     for i in tqdm(data):
#         mean.append(np.mean(i))
#     # print(np.mean(data))
#     mean = np.array(mean)
#     h1 = fits.HDUList([fits.PrimaryHDU(mean)])
#     h1.writeto('data/mean_high_weighted.fits')
#     h2 = fits.HDUList([fits.PrimaryHDU(data)])
#     h2.writeto('data/data_high_weighted.fits')
#     # print(data[0, 0])
# # test()
