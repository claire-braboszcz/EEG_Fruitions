#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:33:46 2020

Splits the spreadshit with information on all trials for all datasets into a per
datatset file 


@author: claire
"""

import pandas as pd
import os.path as op



data_path = '/home/claire/Documents/scripts-local/EEG_Fruitions/Data'

df = pd.read_excel((op.join(data_path, 'fruition_blink.xlsx')))

sessions = df['Raw Filename'].unique()


for sess in sessions:
    
    sess_name = sessions[sess].replace('.eeg', '')  # remove file extension that does not appear on folder name

    events_filename = op.join(data_path, sess_name, 'events.tsv')
    
    sub = df[df['Raw Filename'].str.contains(sess_name)]

    sub.to_csv(events_filename, sep="\t")