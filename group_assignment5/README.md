# Group Assignment 5. Due 11/18, 11:59pm:

Assignment Requirement:  
Consider weather data from the HCN Berkeley station (ID: USC00040693) and the HCN Livermore station (ID: USC00044997) for the time period covered by Ranson's work.  

1. bin the maximum temperature data, separately for the two stations, using the categories Ranson used  
2. devise and implement a stratified permutation test for the hypothesis that the two cities have "the same weather." Formulate the hypothesis as a generalized two-sample problem, i.e., ask whether differences (between the cities) in the number of days each month in which the maximum temperature is in each bin could reasonably be attributed to chance, if the maximum temperatures had been a single population of numbers randomly split across the two cities.  
  * What did you stratify on? Why is that a good choice? Why stratify at all?  
  * Combine results across strata using Fisher's combining function  
  * Can you use the chi-square distribution to calibrate the test? Why or why not?  
3. discuss what this means for Ranson's approach  

Contents:  
- `gs5.ipnyb`: This notebook contains documentation and codes to meet assignment requirements.  
- `gs5.pdf`: This is the pdf version which contains documentation and codes to meet assignment requirements.  
- `TMAX_Berkeley_pivot.csv`: This is a csv file of the results binning the maximum temperature data for Berkeley using the categories Ranson used.
- `TMAX_Livermore_pivot.csv`: This is a csv file of the results binning the maximum temperature data for Livermore using the categories Ranson used.

  
Functions and Tests:    
- `func5.py`: This file contains functions including 'get_stat', 'find_p_value' and 'fisher_comb' which we use in `gs5.ipnyb`.
- `test_func5.py`: This file contains unit tests for functions in `func5.py`.
- `htmlcov`: This html file is the coverage report we generate from `test_func5.py`.

Environment:  
See `stat159.yml` in our home directory.
