#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:44:04 2020

@author: claire
"""


from config import data_path

DOIT_CONFIG = dict(
    default_tasks=['evoked_gng'],
    verbosity=2, sort='alphabetical',
)



def create_events_file():
        """Step 00: Create event file for each dataset using the main spreadsheet """
                
    yield dict(
    file_dep =[data_path, 'fruition_blink.xlsx'], # check if the spreadsheet changed
    actions=['python3 split_spreadsheet.py'],               
    )
      
                  
                  
    