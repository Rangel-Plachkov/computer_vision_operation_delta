# SPARK 2026 Utils

This repository contains all you need to start with the SPARK 2024 Dataset for stream-1 and SPADES dataset for Stream-2.

## Stream 1: spacecraft semantic segmentation

### Dataset structure

Please first create a `data/` folder in `stream-1/`, then download the training and validation datasets in the newly created folder (see dedicated email for download link). After unziping the `*.zip` archives, the tree structure of `data/` must finally follow the one below:

<pre>

└───data/  
    ├───images/
    │	├───object_1/
    │	│	│
    │	│	├───train/
    │	│	│	└───img1....
    │	│	└───val/
    │	│		└───img1....
    │	│
    │	└───object_2/
    │		│
    │		├───train/
    │		│	└───img1....
    │		└───val/
    │			└───img1....
    │	
    │	
    ├───mask/
    │	├───object_1/
    │	│	│
    │	│	├───train/
    │	│	│	└───mask1....
    │	│	└───val/
    │	│		└───mask1....
    │	│
    │	└───object_2/
    │		│
    │		├───train/
    │		│	└───img1....
    │		└───val/
    │			└───img1....
    │	
    ├───train.csv
    └───val.csv
</pre>

The `stream-1/visualize_data.ipynb` notebook contains basic functions to load and display dataset samples.

The correspondences between class names and indexes are given below.

| Class name                | Index    |
|---------------------------|----------|
| `VenusExpress`            | 0        |
| `Cheops`                  | 1        |
| `LisaPathfinder`          | 2        |
| `ObservationSat1`         | 3        |
| `Proba2`                  | 4        |
| `Proba3`                  | 5        |
| `Proba3ocs`               | 6        |
| `Smart1`                  | 7        |
| `Soho`                    | 8        |
| `XMM Newton`              | 9        |


## Stream 2: spacecraft trajectory estimation

The `visualize_events.py` script visualizes event-based spacecraft motion by accumulating all events occurring between consecutive ground-truth timestamps into high-contrast color scheme (White for ON, Blue for OFF). 

It uses quaternions and camera intrinsics to project 3D trajectory axes directly onto the event stream, employing spatial dilation to ensure visibility on high-resolution displays. 

Before executing the script, ensure you have the `h5py`, `pandas`, `opencv-python`, and `scipy` libraries installed, place your `.h5` dataset and `camera.json` in the specified directory, and run `python visualize_events.py` to generate a plot to visualise the labeled poses.

