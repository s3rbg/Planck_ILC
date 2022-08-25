# -*- coding: utf-8 , -*-
"""
Created on Thu Aug 11 10:35:51 2022

@author: Sergio
"""

import numpy as np
from astropy.io import fits
from save_data import save
import numpy.lib.recfunctions as rfn
import pandas as pd
from covariance_regions import covar
from weights import save_weights
from weight_data import weight_data
# def main():
#     path = ['group2_map_detector_F070.fits']
#     save(path, None)
def merge():
    master_path = 'psm_output/output/observations/'
    frecs_low = ['030', '044', '070']
    frecs_high = ['100', '143', '217', '353', '545', '857']
    # frecs_high = ['100', '143', '217', '353']
    paths = []
    for i in frecs_low:
        paths.append(str(master_path)+'LFI/detector_F'+str(i)+'/group2_map_detector_F'+str(i)+'.fits')
    for i in frecs_high:
        paths.append(str(master_path)+'HFI/detector_F'+str(i)+'/group2_map_detector_F'+str(i)+'.fits')
    frecs = np.array(frecs_low+frecs_high, dtype=np.float64)
    save(paths, frecs, 'output2/raw/')    
# merge()

def do_cov():
    data = fits.getdata('output2/raw/data_raw.fits')
    # mean = fits.getdata('output/raw/mean_raw.fits')
    template = fits.getdata('template.fits')
    covar(data, template, 'output2/operators/', 'cov_reg.fits')

def do_weight():
    C = fits.getdata('output2/operators/cov_reg.fits')
    save_weights(C, 'output2/operators/', 'weight_reg.fits')

def comp_weight():
    template = fits.getdata('template.fits')
    w = fits.getdata('output2/operators/weight_reg.fits')
    data = fits.getdata('output2/raw/data_raw.fits')
    weight_data(data, w, template, 'output2/final/', 'data_reg.fits', 'suma_reg.fits')
    
# merge()
do_cov()
do_weight()
comp_weight()

#