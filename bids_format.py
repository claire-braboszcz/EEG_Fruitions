#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:52:08 2020

@author: claire
"""

from mne_bids import write_raw_bids, BIDSPath

from mne_bids.copyfiles import copyfile_brainvision

import mne
import os

from config import (data_path, 
                    bids_root, 
                    subject_ids, 
                   # sessions,
                    tasks, 
                    df_spreadsheet)

import pandas as pd

# create folder for data in BIDS format if it doesnt exist already

if not os.path.exists(bids_root):
    os.makedirs(bids_root)
    
#sessions=[]

#for sess in df_spreadsheet['Raw Filename'].unique():
#    sess= sess.replace('.eeg', '').replace(" ", "_")
#    sessions.append(sess)

session =0

for subj in subject_ids:
    for sess in df_spreadsheet['Raw Filename'].unique():
        session+=1
        for task in tasks:
        # we define filenames that we will use
            ori_sess_name = sess.replace('.eeg', '') # original name
            sess_name = sess.replace('.eeg', '').replace(" ", "_")
            data_orig= os.path.join(data_path, ori_sess_name)
            fname_in = os.path.join(data_orig, ori_sess_name + '.vhdr')  
            
            events_file = os.path.join(data_orig, 'events.tsv')#
            
            # read data and add useful metadata
            
            raw = mne.io.read_raw_brainvision(fname_in, preload=False)
            raw.info['line_freq'] =  df_spreadsheet['Electric Hz'][df_spreadsheet['Raw Filename'] == sess].unique()[0] # specify power line as requiered by BIDS
            raw.info['recording_place'] = df_spreadsheet['Setting'][df_spreadsheet['Raw Filename'] == sess].unique()[0] # keep track of data recording place
            raw.info['recording_date'] = df_spreadsheet['Date'][df_spreadsheet['Raw Filename'] == sess].unique()[0]
            raw.info['recording_time'] = df_spreadsheet['File Saved Time'][df_spreadsheet['Raw Filename'] == sess].unique()[0]

            
                        
            bids_path = BIDSPath(subject = str(subj), 
                                 session = str(session).zfill(2),#sess_name, 
                                 task = task, 
                                 root = bids_root)        
    
           
    
            write_raw_bids(raw, bids_basename, bids_root, event_id=trial_type,
                   events_data=events, overwrite=True)
