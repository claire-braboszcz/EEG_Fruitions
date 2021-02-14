#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:44:04 2020

@author: claire
"""


from config import  (subject_ids, 
                    n_sessions,
                    exclude_sessions, 
                    tasks, 
                    fname, 
                    bandpass_fmin, 
                    bandpass_fmax
                   )

#import pandas as pd
#import os

DOIT_CONFIG = dict(
    default_tasks=['epoch_data'],   # change here the tasks you want to run
    verbosity=2, sort='alphabetical',
)


              
def task_make_derivative_folders():
        """Step 01: Create folder architecture """
        
        for subj in subject_ids:
            for sess in n_sessions:
                if sess in exclude_sessions:
                    continue
                else:
                
                    yield dict(
                            name = "%s-%s" % (subj, sess), 
                            actions=['python3 02_make-derivatives-folders.py %s %s' % (subj, sess)],
                                                                             
                            
                            )

def task_filter_continuuous():
        """Step 02: Filter continuuous data """
        
        for subj in subject_ids:
            for task in tasks:
                for sess in n_sessions:
                    if sess in exclude_sessions:
                        continue
                    else:
                        
                        raw_fname = fname.raw(subject='sub-'+ str(subj).zfill(2), 
                                   session='ses-'+ str(sess).zfill(2), 
                                   task='task-'+ task)
            
            
                        filt_fname=fname.filt(subject='sub-'+ str(subj).zfill(2), 
                                                  session='ses-'+ str(sess).zfill(2), 
                                                  task='task-'+ task, 
                                                  fmin= bandpass_fmin, 
                                                  fmax= bandpass_fmax)
                        
                    
                        yield dict(
                                name = "%s-%s" % (subj, sess), 
                                file_dep =[raw_fname, '03_filter-continuuous-data.py'], 
                                targets=[filt_fname], 
                                actions=['python3 03_filter-continuuous-data.py %s %s %s' % (subj, sess, task)],
                                                                                 
                                
                                )


def task_epoch_data():
        """Step 03: Epoch continuuous data """
        
        for subj in subject_ids:
            for task in tasks:
                for sess in n_sessions:
                    if sess in exclude_sessions:
                        continue
                    else:
                        
                              
            
                        filt_fname=fname.filt(subject='sub-'+ str(subj).zfill(2), 
                                                  session='ses-'+ str(sess).zfill(2), 
                                                  task='task-'+ task, 
                                                  fmin= bandpass_fmin, 
                                                  fmax= bandpass_fmax)
                        
                        epochs_fname=fname.epochs(subject='sub-'+ str(subj).zfill(2), 
                                                  session='ses-'+ str(sess).zfill(2), 
                                                  task='task-'+ task, 
                                                  )
                    
                        yield dict(
                                name = "%s-%s" % (subj, sess), 
                                file_dep =[filt_fname, '03_filter-continuuous-data.py'], 
                                targets=[epochs_fname], 
                                actions=['python3 04_epoch-data.py %s %s %s' % (subj, sess, task)],
                                                                                 
                                
                                )


    