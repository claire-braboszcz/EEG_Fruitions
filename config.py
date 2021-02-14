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

bids_root_der = os.path.join(bids_root, 'derivatives')

reports_dir = os.path.join(bids_root_der, 'reports')

df_spreadsheet = pd.read_excel((os.path.join(data_path, 'fruition_blink_tmp.xlsx')))

tasks = ['fruitions']
subject_ids = ['01']

# define sesssions name from spreadsheet
n_sessions =range(1,29)
exclude_sessions = [14, 22]

#for sess in df_spreadsheet['Raw Filename'].unique():
#    sess= sess.replace('.eeg', '').replace(" ", "_")
#    sessions.append(sess)



###############################################################################
# STUDY Pre processing and analysis parameters
###############################################################################


# filter parameters 
bandpass_fmin = 0.1
bandpass_fmax = None



#########################################################################################
 # Parameters for creating epochs

#########################################################################################
# epochs characteristics

tmin, tmax = -20, 20

baseline=None




###############################################################################
# Templates for filenames
#############################################################################
# This part of the config file uses the FileNames class. It provides a small
# wrapper around string.format() to keep track of a list of filenames.
# See fnames.py for details on how this class works.
fname = FileNames()

# filename for folders
fname.add('bids_root', bids_root)
fname.add('folder_preproc', bids_root_der + '/eeg_preprocess/{subject}/{session}/eeg/') # folder name and path to store pre-processed files
fname.add('reports_dir', reports_dir)



#filenames for files generated during analysis
fname.add('raw','{bids_root}/{subject}/{session}/eeg/{subject}_{session}_{task}_eeg.vhdr')


fname.add('filt','{folder_preproc}/{subject}_{session}_{task}_filt_{fmin}_{fmax}_raw.fif')
fname.add('epochs','{folder_preproc}/{subject}_{session}_{task}_epo.fif')


# Filenames for MNE reports

#fname.add('report', '{reports_dir}/{subject}_{session}_{task}_report.h5')
fname.add('report_html', '{reports_dir}/{subject}_{session}_{task}_report.html')

