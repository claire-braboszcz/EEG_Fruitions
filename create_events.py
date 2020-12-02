import os.path as op
import os
import numpy as np
import mne
from mne_bids.copyfiles import copyfile_brainvision
import pandas as pd


data_path='/home/claire/Documents/scripts-local/EEG_Fruitions/Data'


vhdr_file = op.join(data_path, 'EEG BG2 DMI Day 10.vhdr')
vhdr_file_renamed = op.join(data_path, 'EEGBG2DMI_Day10.vhdr')

copyfile_brainvision(vhdr_file, vhdr_file_renamed, verbose=True)


raw = mne.io.read_raw_brainvision(vhdr_file)

events= pd.read_excel('fruition_blink.xlsx')

#get annotations corresponding to current eeg file
my_events = events[events['Raw Filename'].str.contains('EEG BG2 DMI Day 10.eeg')]


my_events

#use mne.read_annotations to create mne.annotation object


my_annot = mne.Annotations(onset = my_events['Location (s)'], 
                         duration = [1, 1, 1, 1, 1, 1, 1], 
                         description= ['F','F','F', 'F', 'F', 'F', 'F'])

my_annot

# add annotations to raw object
raw.set_annotations(my_annot)

print(raw.annotations)

# create events from annotations
# can be used to epoch data
events, _ = mne.events_from_annotations(raw, event_id= dict(F=1))

# plot raw with events
raw.plot(events=events)

