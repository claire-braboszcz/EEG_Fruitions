#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:13:15 2020

===================
EEG Fruition config file
===================

Configuration parameters for the EEG Fruitions project

adapted from https://github.com/AaltoImagingLanguage/conpy/tree/master/scripts

@author: claire
"""

import os
import pandas as pd
from fnames import FileNames



data_path='/home/claire/Documents/scripts-local/EEG_Fruitions/Data'

bids_root = os.path.join(data_path, 'EEG-Fruitions-BIDS')

df_spreadsheet = pd.read_excel((os.path.join(data_path, 'fruition_blink.xlsx')))

tasks = ['fruitions']
subject_ids = [1]

# define sesssions name from spreadsheet
sessions=[]

for sess in df_spreadsheet['Raw Filename'].unique():
    sess= sess.replace('.eeg', '').replace(" ", "_")
    sessions.append(sess)



###############################################################################
# Templates for filenames
#############################################################################
# This part of the config file uses the FileNames class. It provides a small
# wrapper around string.format() to keep track of a list of filenames.
# See fnames.py for details on how this class works.
fname = FileNames()

