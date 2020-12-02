#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:13:15 2020

===================
EEG Fruition config file
===================

Configuration parameters for the EEG Fruitions project

adapted from https://github.com/AaltoImagingLanguage/conpy/tree/master/scripts

@author: claire
"""


from fnames import FileNames




data_path='/home/claire/Documents/scripts-local/EEG_Fruitions/Data'


sessions = [3, 
            9, 
            10, 
            13, 
            17, 
            19]




###############################################################################
# Templates for filenames
#############################################################################
# This part of the config file uses the FileNames class. It provides a small
# wrapper around string.format() to keep track of a list of filenames.
# See fnames.py for details on how this class works.
fname = FileNames()

