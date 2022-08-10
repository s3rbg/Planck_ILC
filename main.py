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
    maps = fits.getdata('data/data_high.fits')
    mean = fits.getdata('data/mean_high.fits')
    cov(maps, mean, 'data/cov_high.txt')
    # print('\n')
    # print(C)


def test_map():
    cmb = read_map('psm_output/output/components/cmb/cmb_map.fits', dtype=np.float64)
    means_w = fits.getdata('data/mean_weighted.fits')*1e6
    # data = fits.getdata('data/data_high.fits')
    means = fits.getdata('data/mean_high.fits')*1e6
    plot.mollview(means_w)
    plot.mollview(means)
    plot.mollview(cmb)
    # plot.gnomview(data[:,2])
    # plot.gnomview(means)
    # plot.gnomview(cmb)
    print('stdev CMB sim: ', np.std(cmb), 'uK')
    print('stdev map weighted: ', np.std(means_w), 'uK')
    print('stdev map: ', np.std(means), 'uK')
    # print(np.mean(cmb))
    # print('stdev map: ' np.std(means), 'uK')
test_map()
# main()
