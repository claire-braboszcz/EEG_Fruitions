

# EEG Fruition project

The data and folder architecture follows the EEG-BIDS format. 
  

The data processing pipeline uses doit automation tool (https://pydoit.org/).

The tasks to run need to be specified at the start of the `dodo.py` script. 
To execute, open a terminal from the parent folder an types in 'doit'.

The `config.py` file contains the paths and parameters used for preprocessing the data (eg. filter bandpass, epochs length etc.).

## Epochs

In the `04_epoch-data.py` file the events are imported from the excel spreadsheet before epoching the data. 
The events are named as "Trial types/Grade/Door". This way in subsequent analysis it will be easy to select trials based on these 3 parameters.

