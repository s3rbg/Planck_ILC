#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 16:21:45 2022

@author: sergio
"""

import numpy as np
import healpy as hp
from healpy.fitsfunc import read_map
from healpy import visufunc as plot
from astropy.io import fits
import os
from tqdm import tqdm
from covariance import cov
# def save(file, data):
#     if not os.path.exists(file):
#         with open(file, 'w') as f:
            
def main():
    maps = fits.getdata('data/data.fits')
    mean = fits.getdata('data/mean.fits')
    cov(maps, mean, 'data/cov.txt')
    # print('\n')
    # print(C)

main()
