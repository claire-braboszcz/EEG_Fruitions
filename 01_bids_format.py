#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:52:08 2020

@author: claire
"""

from mne_bids import write_raw_bids, BIDSPath

from mne_bids.copyfiles import copyfile_brainvision
#import argparse
import mne
import os

from config import (data_path, 
                    bids_root, 
                    subject_ids, 
                   # sessions,
                    tasks, 
                    df_spreadsheet
                    )
                
import numpy as np
import pandas as pd


# Handle command line arguments = get variables from the dodo script
#parser = argparse.ArgumentParser(description=__doc__)
#parser.add_argument('subject', metavar='subj', help='The subject to process')
#parser.add_argument('session', metavar='sess', help='The session to process')
#parser.add_argument('task', metavar='task', help='The task to process')
#
#args = parser.parse_args()
#subj= args.subject
#sess= args.sess_name
#task = args.task
#df_spreadsheet = args.df_spreadsheet



for subj in subject_ids:
        for sess in df_spreadsheet['Raw Filename'].unique():
            for task in tasks:


                
                session = int(df_spreadsheet['Session'][df_spreadsheet['Raw Filename'] == sess].unique()[0])
                
                print('Processing subject:', subj, 'session:', sess)
                
                # create folder for data in BIDS format if it doesnt exist already
                
                if not os.path.exists(bids_root):
                    os.makedirs(bids_root)
                 
                    
                #df_spreadsheet = pd.read_excel((os.path.join(data_path, 'fruition_blink.xlsx')))        
                #sessions=[]
                
                #for sess in df_spreadsheet['Raw Filename'].unique():
                #    sess= sess.replace('.eeg', '').replace(" ", "_")
                #    sessions.append(sess)
                
                
                        # we define filenames that we will use
                ori_sess_name = sess.replace('.eeg', '') # original name
                sess_name = sess.replace('.eeg', '').replace(" ", "_")
                data_orig= os.path.join(data_path, ori_sess_name)
                fname_in = os.path.join(data_orig, ori_sess_name + '.vhdr')  
                
                
                bids_path = BIDSPath(subject = str(subj).zfill(2), 
                                     session = str(session).zfill(2),#sess_name, 
                                     task = task, 
                                     root = bids_root)        
                
                
                # rename brainvision file
                vhdr_ori = fname_in
                vhdr_new= os.path.join(data_orig, bids_path.basename + '.vhdr')
                copyfile_brainvision(vhdr_ori, vhdr_new, verbose=True)
                
               
                
                
                
                
                # add annotations to raw object
                raw = mne.io.read_raw_brainvision(vhdr_new, preload=False)
                
                
                             
                #------------------------------
                
                # read data and add useful metadata
                
                # WARNING: these did not save as it does not correspond to field in the FIF standard - this information is still available in the fruition_blink spreadsheet
                
                raw.info['line_freq'] =  int(df_spreadsheet['Electric Hz'][df_spreadsheet['Raw Filename'] == sess].unique()[0]) # specify power line as requiered by BIDS
                raw.info['recording_place'] = df_spreadsheet['Setting'][df_spreadsheet['Raw Filename'] == sess].unique()[0] # keep track of data recording place
                raw.info['recording_date'] = df_spreadsheet['Date'][df_spreadsheet['Raw Filename'] == sess].unique()[0]
                raw.info['recording_time'] = df_spreadsheet['File Saved Time'][df_spreadsheet['Raw Filename'] == sess].unique()[0]
                
                
                # set channel locations
                
                
                raw.set_montage('standard_1020', 'on_missing', 'warn')    
                #raw.plot_sensors()
                            
                write_raw_bids(raw, bids_path, overwrite=True, verbose=True)

