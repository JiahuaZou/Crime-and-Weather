# Group Assignment 2. Due 11/4, 11:59pm:

Assignment Requirements
- Construct a grid of (lat, long) points within Alameda county separated by approximately 5 miles. The first point should be at (37.905098, -122.272225), near Summit Reservoir.
- Write code to identify all weather stations within $x$ miles of Alameda County
- Identify all weather stations within 10 miles (not Ranson's 50 miles) of any of the grid points in Alameda county, and find the weighted average inverse distance from each station to the points in the county grid. Your code for finding the stations should take the distance range as an input parameter (i.e., your code should let you find all stations within 5 miles or 50 miles, too).

Prerequisites
- install geopy using command `pip install geopy`
- install shapely using command `conda install shapely` or `pip install shapely`
- `time`, `pathlib`, and `csv` are built-in python module

Contents
- `gs2.ipnyb`: This file contains documentation and codes to go through the whole process of constructing grid points within Alameda, identifying all stations within $x$ miles of Alameda, and obtaining weighted average inverse distance from each station to grid points. 

- `Assignment_2_Functions.py`: This file contains find_optimal function which finds the amount of latitude and longitude corresponding to 5 miles adjusted by earth curvature; within_alameda function to identify wheather a point is within x files of Alameda; idwa function which finds the weighted average inverse distance.  

- `find_grid_points.ipynb`: This file contains codes to then extracts all grid points over Alameda county. 

- `grid_points_alameda.csv`: This file contains information (name, latitude, longitude) of all grid points within Alameda county, by running codes from find_grid_points.ipynb file. We save grid points information into a csv for future use to avoid running time-consuming functions.

- `stations_within_10miles_alameda.csv`: This file contatins information of all weather stations within 10 miles of Alameda county, extracted by using within_alameda function.

- `coverage_report.html`: This html file is the coverage report we generate from `test_assign02_functions.py`.

Running Tests
Please run `test_assign02_functions.py` to test functions from `Assingment_2_Functions.py`
