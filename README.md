# Star Cluster Simulation Analysis Project

USU cs5040/6040 group 10

Marcus Quincy, Reagan Baxter, Eli Peterson

## Data and Results

This project is to create visualizations from the [Star Cluster Simulation
Data](https://www.kaggle.com/datasets/mariopasquato/star-cluster-simulations/data).
It is a set of 19 csv files.

Some of the main goals of the project are to analyze which stars escape and also
gain a better visualization of the sparse data set.

The main tools used for this are ParaView (https://www.paraview.org/) and
python.

### Description of files in this repo

- animations/
    - Directory containing various video animations of the data.

- csvs/
    - data/
        - Directory containing the original data (with .bak extension), the and
          the results of running the preprocess script both with separating the
          escapees out, and with standard preprocessing. This directory can be
          used as input to escapeesColor.pvsm.
    - escaped-interpolated/
        - Directory containing the csvs which are the output of running the
          cubic-interpolation script. This directory can be in input to
          escapee-cubic-interpolated.pvsm.
    - splitData/
        - Directory containing data split into two groups: one with ID and one
          without. The data here is input to escapeeSpeed.pvsm and
          EscapeesTemporalInterpolated.pvsm.

- stateFiles/
    - escapee-cubic-interpolated.pvsm
        - ParaView state file for creating an animation of the escaped stars with
          cubic interpolation. Expects data to be preprocessed by
          cubic-interpolation script first.
    - subset-cubic-interpolation-animated.pvsm
        - ParaView state file for creating an animation of random stars with cubic
          interpolation. Expects data to be preprocessed by cubic-interpolation
          script first.
    - escapeesColor.pvsm
        - ParaView state file coloring escaped stars green through all the time
          steps. Requires escapees to be separated using preprocess script first.
    - escapeeSpeed.pvsm
        - ParaView state file which analyzes the speeds of the stars that escape.
          Requires data to be processed by Split.py first.
    - EscapeesTemporalInterpolated.pvsm
        - State file with just the stars that escape and uses Temporal
          Interpolation to visualize their movements. Requires data to be
          processed by Split.py first.
    - temporalInterpolator.pvsm
        - State file with temporal interpolation applied to the entire data set.
          Uses the base data set.

- python/
    - Centroid.py
        - Uses data processed by fixMissingIds.py or preprocess as input. This
          script calculates the mean of all the data for visualization.
    - cubic-interpolation
        - Takes the output of preprocess script as input. This script takes the
          data and outputs a data set with more time steps with cubic
          interpolation applied.
    - fixMissingIds.py
        - Adds id's to the data to compensate for all the stars missing data.
    - speedPlot.py
        - Plots the speeds of the stars in relation to the time steps. Uses the
          output of the Split.py script.
    - Split.py
        - Splits the data into escapees and nonescapees.

## Steps to reproduce

### Requirements

- ParaView (5.11 required for cubic interpolation animation state file)
- python3
- numpy
- scipy
- pandas
- seaborn
- matplotlib

All these can be installed via `guix shell -m manifest.scm`.

### Pre Process the data

Note: most of the processed data has been saved already in the repository.

**Cubic Interpolation**

First missing ids (escapees) need to be populated back into the csv files. This
is done with the preprocess script. (If cloned this repo this step is done for
you...)
```
./python/preprocess -i.bak --separate-escapees csvs/data/c_*.csv
```
This will also copy the data for the ids that escape into another set of csv
files. The output of these files will be in the same directory that the files
were originally in.

For cubic interpolation run the following. This will create ~700MB of data for
the entire csv set. For example to generate cubic interpolation data for the
escaped stars with a time step every 0.02 time steps of the original run:
```
./python/cubic-interpolation -n 0.02 -o <output dir> <path to csv e.g. csvs/data/escapee_c_*>
```

**Centroids**

For Centroid calculation, first edit the input and output files in the source
file to the desired location then run `python python/Centroid.py`. The tail of the file
should look like:

```python
if __name__ == "__main__":
    input_dir = "csvs/splitData"  # Change this to the input directory containing CSV files
    output_dir = "my-output-dir"  # Specify the output directory to save centroid CSV files

    process_csv_files(input_dir, output_dir)
```

**Plots**

To view the plots analyzing the data:
```
python3 python/speedPlot.py
```

This will use matplotlib to visualize the data.

### Load the Paraview state files

Now with the data processed, the Paraview [state files](./stateFiles/) can be
loaded. Be sure to select the data manually instead of using the paths in the
state file. Which CSV files are expected to be associated with each ParaView
file is described in the "Description of files in this repo" section above (note
not all CSV files are part of the repo to prevent it from getting bigger than it
already is).
