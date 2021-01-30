#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:55:12 2021

@author: claire
"""

from mne_bids import BIDSPath, read_raw_bids

from config import (subject_ids, 
                    n_sessions, 
                    tasks,
                    bids_root,
                    exclude_session
                    )


for subj in list(subject_ids):
    for sess in list(range(1, n_sessions+1)):
        if sess in exclude_session:
            continue
        
        else:
            for task in tasks:
        
                bids_path = BIDSPath(subject = subj, 
                                         session = str(sess).zfill(2),#sess_name, 
                                         task = task, 
                                         root = bids_root)        
                    