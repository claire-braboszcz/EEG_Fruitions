#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:02:17 2021

@author: claire
"""

import mne
from config import (fname, 
                    bandpass_fmin, bandpass_fmax, 
                    df_spreadsheet, 
                    tmin, tmax, 
                    baseline)
import argparse
import numpy as np
from mne.preprocessing import ICA, create_ecg_epochs, create_eog_epochs


# Handle command line arguments
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('subject', metavar='subj', help='The subject to process')
parser.add_argument('session', metavar='sess', help='The session to process')
parser.add_argument('task', metavar='task', help='The task to process')

args = parser.parse_args()
subj= args.subject
sess= args.session
task= args.task




print('Process data for subject:', subj, 'session:', sess)

subject='sub-'+ str(subj).zfill(2)
session='ses-'+ str(sess).zfill(2)
task='task-'+ task


raw = mne.io.read_raw_fif(fname.filt(
                                   subject=subject, 
                                   session=session,
                                   task= task, 
                                   fmin=bandpass_fmin, 
                                   fmax=bandpass_fmax),  preload=True)  



#------------------------------------------
# Insert events from spreadsheet in raw
#------------------------------------------
# specify the trial type
df_spreadsheet['trial'] = np.where(df_spreadsheet['Grade'] != 'NF Blink', 'F', 'NF')
df_spreadsheet['Door']=df_spreadsheet['Door'].replace(np.nan, 'NF')

df_spreadsheet['trial_type'] = df_spreadsheet['trial'] + '/' + df_spreadsheet['Grade'] + '/' + df_spreadsheet['Door'] 
#df_spreadsheet['trial_type']=df_spreadsheet['trial_type'].replace(np.nan, 'NF')
#get annotations corresponding to current eeg file
my_annot = mne.Annotations(onset =  df_spreadsheet['Location (s)'][df_spreadsheet['Session'] == int(sess)], 
                         duration = 1, 
                         description= df_spreadsheet['trial_type'][df_spreadsheet['Session'] == int(sess)], 
                         )


raw.set_annotations(my_annot)

#print(raw.annotations)

# create events from annotations
# can be used to epoch data
events, event_id = mne.events_from_annotations(raw)


#------------------------------
# Find onsets of blinks based on Fp1 activity. Create epochs around them

# Passive viewing Task
print('Epoch the data ')


epochs = mne.Epochs(raw, events, event_id= event_id, tmin=tmin, tmax=tmax, baseline=baseline,  preload=True)


epochs.save(fname.epochs(subject = subject, session= session, task= task), overwrite = True)

















