# Group Assignment 6. Due 12/2, 11:59pm:

Assignment Requirements

* fit the Poisson regression model to the data for all of Alameda County, and for the two pieces of Alameda county separately. Fit the separate estimates simultaneously, including dummy variables for all of Alameda county (treat Alameda County as a whole the way Ranson treated states; East and West Alameda are the two counties in the State of Alameda).

* devise and perform a permutation test to check whether the two pieces of Alameda county are consistent with a single model.

Prerequisites

* install crypto random version 3.7.2 using command pip install pycryptodome


Contents:
* `ga6.ipynb`: This file contains notebook that records methods and explanations to fit Poisson regression model and permutation test.
	* Try to fit poisson model for whole alameda county. First to contrust a 359 rows * 55 columns data frame contains 8 max temperatutre bins( 30–39F, 40–49F, 50–59F,..., 90–100F, and large and equal than 100 F), 5 prcp bins ( 0mm, 1–4mm, 5–14 mm, 15–29 mm, and large and equal than 30 mm), 30 theta dummy varibles (from 1980 to 2009), and 12 phi dummy varibles (from Januarary to December) by calling helper functions in Assignment6_functions.py. By using generalized linear model in statsmodels.api package to fit poisson model.
    * Then repeat what have done for whole alameda county to fit poisson model for west and east alameda. A small change is that for east and west alameda, there are only three prcp bins ( 0mm, 1–4mm, 5–14 mm). The dataframe bocomes to 359 rows * 52 columns.
    * After fitting poission model. Use PRNG random number generator and to do  permutation test. Finally, calculate the p value after 1000 runs is 0.013 which is significant (less than 0.05).

*  `ga6.pdf`: This is the pdf version which contains documentation and codes to meet assignment requirements.
    
* `all_alameda_crime.csv`, `east_alameda_crime.csv`, `west_alameda_crime.csv`: These three csv files contain total crime numbers from 198001  to 200912 correspond to whole alameda county, east alameda county, and west alameda county. These three files will be used when to fit poission model, total crime numbers for each month will be treated as response variable y.

* `clean_data.py`: This file contains function to clean crime data to first choose time range from 198001 to 200912. In total of 360 rows, which are 30 years times 12 months. Then summarize total number of crimes for each month, etc. 

* `Assignment6_functions.py`: This file contains six helper function for preparing poission model and permutation test such as get_temp_features, get_prcp_features_whole，get_prcp_features, get_dummy_features, get_permute, and rms. 

* `test_func6.py`: This file test functions in clean_data.py and Assignment6_functions.py.
* `htmlcov`: This folder contains test coverage report generated from test_func6.py and coverage rates reach to 100%.


Environment

* See `stat159.yml` in our home directory.





