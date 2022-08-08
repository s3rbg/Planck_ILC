#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:48:15 2022

@author: sergio
"""

from save_data import save

def saver():
    master = 'psm_output/output/observations/LFI/'
    path30 = str(master)+'detector_F030/group2_map_detector_F030.fits'
    path44 = str(master)+'detector_F044/group2_map_detector_F044.fits'
    path70 = str(master)+'detector_F070/group2_map_detector_F070.fits'
    paths = [path30, path44, path70]
    # print(paths)
    aux = save(paths)
    # print(len(aux))
    # print(aux[0, :])
    # for i in aux[:10]:
        # print(i)

# saver()