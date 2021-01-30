#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:44:04 2020

@author: claire
"""


from config import (data_path, 
                    bids_root, 
                    subject_ids, 
                   # sessions,
                    tasks, 
                    df_spreadsheet
                   )

#import pandas as pd
#import os

DOIT_CONFIG = dict(
    default_tasks=['make_bids'],
    verbosity=2, sort='alphabetical',
)


#
#def create_events_file():
#        """Step 00: Create event file for each dataset using the main spreadsheet """
#                
#        yield dict(
#        file_dep =[data_path, 'fruition_blink.xlsx'], # check if the spreadsheet changed
#        actions=['python3 00-split_spreadsheet.py'],               
#    )
#      
                  
def task_filter():
    