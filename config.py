#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:13:15 2020

===================
EEG Fruition config file
===================

Configuration parameters for the EEG Fruitions project.
Specifies variables for running tasks from the dodo.py files, as well as for using
in each scripts.

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
# note this tmp file excludes lines corresponding from session 14 and 22 that were throwing an error
# use the exclude_session parameter when looping through sessions from the fruition_blink.xlsx file 

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



#filenames for files generated during analysis
fname.add('raw','{bids_root}/{subject}/{session}/eeg/{subject}_{session}_{task}_eeg.vhdr')


fname.add('filt','{folder_preproc}/{subject}_{session}_{task}_filt_{fmin}_{fmax}_raw.fif')
fname.add('epochs','{folder_preproc}/{subject}_{session}_{task}_epo.fif')



