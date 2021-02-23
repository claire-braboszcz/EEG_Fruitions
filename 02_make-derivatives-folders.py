#!/usr/bin/env python
# coding: utf-8

# In[ ]:

"""
Create BIDS-compatible derivatives folder for each participant. 
You can adapt and run this function if you want to create new derivatives folders.
New folders name and paths should be added to the fname structure from config.py file.

"""

import os

from config import (fname, bids_root, bids_root_der)
import argparse



# Handle command line arguments
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('subject', metavar='subj', help='The subject to process')
parser.add_argument('session', metavar='sess', help='The session to process')

args = parser.parse_args()
subj= args.subject
sess= args.session


if not os.path.exists(bids_root_der):
    os.makedirs(bids_root_der)


print('Making folders for subject:', subj, 'session:', sess)



f_preproc=fname.folder_preproc(bids_root_der=bids_root_der, 
                               subject='sub-'+ str(subj).zfill(2), 
                               session='ses-'+ str(sess).zfill(2))



if not os.path.exists(f_preproc):
    os.makedirs(f_preproc)



