#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:37:39 2022

@author: sergio
"""
import healpy as hp
from healpy.fitsfunc import read_map
from astropy.io import fits
import numpy as np


def reminder(cmb, mapa, title):
    rem_map = mapa-cmb
    hp.mollview(rem_map, norm='hist', title=title, unit='uK')
    print('Mean '+str(title)+' = '+str(np.mean(rem_map)))
    print('StDev '+str(title)+' = '+str(np.std(rem_map)))

file = 'psm_output/output/components/cmb/cmb_map.fits'

cmb = read_map(file)

map_full = fits.getdata('output2/final/suam_fin.fits')*1e6
map_region = fits.getdata('output2/final/suma_reg.fits')*1e6

mask_raw = read_map('Mask.fits', nest=True)
maska = hp.pixelfunc.ud_grade(mask_raw, 1024, order_in='NESTED', order_out='RING').astype(np.bool_)

cmb_mask = hp.ma(cmb)
cmb_mask.mask = np.logical_not(maska)

map_full_mask = hp.ma(map_full)
map_full_mask.mask = np.logical_not(maska)

map_region_mask = hp.ma(map_region)
map_region_mask.mask = np.logical_not(maska)

reminder(cmb_mask, map_full_mask, 'Full Sky')
reminder(cmb_mask, map_region_mask, 'Regions')
