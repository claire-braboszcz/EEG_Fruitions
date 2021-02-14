

# EEG Fruition project

The data and folder architecture follows the EEG-BIDS format (script `01_bids_formats`). 
  

## Configuration  

The data processing pipeline uses doit automation tool (https://pydoit.org/).

EEG are processed using MNE-Python v0.22.0 (https://mne.tools/stable/index.html).

## Pipeline

The tasks to run need to be specified at the start of the `dodo.py` script. 
To execute, open a terminal from the parent folder an types in 'doit'.

The `config.py` file contains the paths and parameters used for preprocessing the data (eg. filter bandpass, epochs length etc.).

If more sessions or subjects are added, the `n_sessions` and `subject_ids` variable need to be modified in `config.py`. 

NB: for now the files from sessio  14 and 22 could not be opened (maybe an issue with renaming the raw files at some point).

## Filter
The type of filter used can be modified in the `03_filter-continuuous-data.py` file.
Filter parameters such as bandpass frequencies can be modified in the `config.py` file (bandpass_fmin, bandpass_fmax)

## Epochs

In the `04_epoch-data.py` file the events are imported from the excel spreadsheet before epoching the data. 
The events are named as "Trial types/Grade/Door". This way in subsequent analysis it will be easy to select trials based on these 3 parameters.

The length of epochs can be changed using the parameters tmin and tmax in `config.py`

## EEGLAB

The raw data can be loaded in EEGLAB using the load EEG-BID function. Note that the raw data do not contain the events and would requiere to write a specific matlab script to add them.

The epoch data (in `.fif` format) can be loaded in EEGLAB using the 'File IO' menu (or `pop_fileio` function). 