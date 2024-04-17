# Star Cluster Simulation Analysis Project

USU cs5040/6040 group 10

## The data

This project is to create visualizations from the [Star Cluster Simulation Data](https://www.kaggle.com/datasets/mariopasquato/star-cluster-simulations/data). It is a set of 19 csv files.  

## Pre Process the data

Note: most of the processed data has been saved already in the repository.

First missing ids (escapees) need to be populated back into the csv files. This is done with the preprocess script.  
```
./preprocess -i.bak --separate-escapees *.csv
```
This will also copy the data for the ids that escape into another set of csv files.  

For cubic interpolation run the following. This will create ~700MB of data for just the escapee csv set.
```
./cubic-interpolation -n 0.02 -o <output dir> <path to csv e.g. data/escapee_c_*>
```

For Centroid calculation, first edit the input and output files to the desired location then run `pyhton Centroid.py`


## Load the Paraview state files
Now with the data processed, the Paraview [state files](./stateFiles/) can be loaded. Be sure to select the data manually instead of using the paths in the state file. 
