#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:48:37 2022

@author: sergio
"""

from healpy.fitsfunc import read_map
import healpy as hp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
from astropy.io import fits
from uncertainties import ufloat
def f(x, a, b):
    return a*x + b

def fit(f, x, y):
    popt, pcov = cf(f, x, y)
    return popt, np.sqrt(np.diag(pcov))

def tt_plot(cmb, result, mini, maxi, title):
    popt, pcov = fit(f, cmb, result)
    plt.plot(cmb, result, 'b.', label='data')
    x = np.linspace(mini, maxi, 1000)
    y = f(x, popt[0], popt[1])  
    plt.plot(x, y, 'k-', label='fit')
    plt.axis('equal')
    plt.legend()
    plt.grid()
    plt.show()
    return popt, pcov

file = 'psm_output/output/components/cmb/cmb_map.fits'
# cmb = read_map('Mapa_CMB.fits', nest=True)
# cmb = hp.pixelfunc.ud_grade(cmb, 1024, order_in='NESTED', order_out='RING')*1e6
cmb = read_map(file)
hp.mollview(cmb, norm='hist', title='CMB')
plt.show()
suma = fits.getdata('output2/final/suam_fin.fits')*1e6
suma_reg = fits.getdata('output2/final/suma_reg.fits')*1e6

mask_raw = read_map('Mask.fits', nest=True)
maska = hp.pixelfunc.ud_grade(mask_raw, 1024, order_in='NESTED', order_out='RING').astype(np.bool_)

suma_mask = hp.ma(suma)
suma_mask.mask = np.logical_not(maska)
suma_reg_mask = hp.ma(suma_reg)
suma_reg_mask.mask = np.logical_not(maska)
cmb_mask = hp.ma(cmb)
cmb_mask.mask = np.logical_not(maska) 

hp.mollview(cmb_mask, norm='hist', title='CMB')
plt.show()
hp.mollview(suma_mask, norm='hist', title='Full sky')
plt.show()
hp.mollview(suma_reg_mask, norm='hist', title='Regions')
plt.show()

popt, pcov = tt_plot(cmb_mask, suma_mask, -400, 400, 'Full Sky')
a = ufloat(popt[0], abs(pcov[0]))
b = ufloat(popt[1], abs(popt[1]))
print(a, b)

popt_reg, pcov_reg = tt_plot(cmb_mask, suma_reg_mask, -400, 400, 'Regions')
a_reg = ufloat(popt_reg[0], abs(pcov_reg[0]))
b_reg = ufloat(popt_reg[1], abs(popt_reg[1]))
print(a_reg, b_reg)

plt.plot(cmb_mask, suma_mask, 'r.', label='full_map')
plt.plot(cmb_mask, suma_reg_mask, 'b.', label='Divided map', alpha=0.01)
plt.grid()
plt.legend()
plt.show()
