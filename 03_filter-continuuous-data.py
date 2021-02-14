#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:55:12 2021

@author: claire
"""

import os
import mne
from config import (fname, 
                    bandpass_fmin, bandpass_fmax)
import argparse



# Handle command line arguments
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('subject', metavar='subj', help='The subject to process')
parser.add_argument('session', metavar='sess', help='The session to process')
parser.add_argument('task', metavar='task', help='The task to process')

args = parser.parse_args()
subj= args.subject
sess= args.session
task= args.task




print('Filter data for subject:', subj, 'session:', sess)

subject='sub-'+ str(subj).zfill(2)
session='ses-'+ str(sess).zfill(2)
task='task-'+ task


raw = mne.io.read_raw_brainvision(fname.raw(
                                   subject=subject, 
                                   session=session,
                                   task= task),  preload=True)  

filt_raw =  raw.copy()


# specify the filter
filt_raw.load_data().filter(l_freq=bandpass_fmin, h_freq=bandpass_fmax, l_trans_bandwidth='auto',
        h_trans_bandwidth='auto', filter_length='auto', phase='zero',
        fir_window='hamming', fir_design='firwin')


# save the filtered data
f=fname.filt(subject = subject, session= session, task= task, fmin=bandpass_fmin, fmax=bandpass_fmax)

filt_raw.save(f, overwrite = True)

