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
from covariance1 import save_cov
from weights import save_weights
from weight_data import weight_data
# def main():
#     path = ['group2_map_detector_F070.fits']
#     save(path, None)
def do_means():
    master_path = 'psm_output/output/observations/LFI/'
    frecs = ['030', '044', '070']
    paths = []
    for i in frecs:
        paths.append(str(master_path)+'detector_F'+str(i)+'/group2_map_detector_F'+str(i)+'.fits')
    frecs = np.array(frecs, dtype=np.float64)
    save(paths, frecs)    

def do_cov():
    data = fits.getdata('data/data.fits')
    mean = fits.getdata('data/mean.fits')
    save_cov(data, mean, n_it = 1024)
# do_cov()
def do_weight():
    C = fits.getdata('data/weight2/Cov.fits')
    save_weights(C)

def comp_weight():
    data = fits.getdata('data/weight2/data_exp.fits')
    w = fits.getdata('data/weight2/w.fits')
    data_raw = fits.getdata('data/data.fits')
    weight_data(data, w, data_raw)
comp_weight()
# do_weight()
# do_cov()
# c = a[0:1]
# b = np.concatenate((a, a[0:1]))
# b = np.array([[5, 6],
#               [7, 8]], dtype=np.float64)
# c = [a, b]
# # h1 = fits., HDUList([fits.PrimaryHDU(c)])
# # h1.writeto('test.fits')
# data = fits.getdata('test.fits')


# e = rfn.append_fields(c, '3', np.empty(c.shape[0], dtype=np.float64), dtypes=np.float64)
# main()
# a = np.rec.array([((9,5.),(2, 3)),((2,3.),(4,5))],
#                  dtype=[('i', np.float64), ('loc', np.float64)])

# new_dt = np.dtype(a.dtype.descr + [('test', np.float64)])
# b = rfn.append_fields(a, 'USNG', np.empty(a.shape[0], dtype=np.float64), dtypes=np.float64)

# b = a.field('i')
# c = a.field('loc')