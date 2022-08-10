#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 12:48:15 2022

@author: sergio
"""

from save_data import save

def saver():
    master = 'psm_output/output/observations/HFI/'
    frecs = [217, 353, 545]
    path0 = str(master)+'detector_F'+str(frecs[0])+'/group2_map_detector_F'+str(frecs[0])+'.fits'
    path1 = str(master)+'detector_F'+str(frecs[1])+'/group2_map_detector_F'+str(frecs[1])+'.fits'
    path2 = str(master)+'detector_F'+str(frecs[2])+'/group2_map_detector_F'+str(frecs[2])+'.fits'
    paths = [path0, path1, path2]
    # print(paths)
    aux = save(paths, frecs, data_file='data_high.fits', data_file_mean='mean_high.fits')
    # print(len(aux))
    # print(aux[0, :])
    # for i in aux[:10]:
        # print(i)


saver()