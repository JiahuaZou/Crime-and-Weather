# Group Assignment 3. Due 11/4, 11:59pm:

Assignment Requirements

* retrieve the weather data for the relevant time periods for stations within 10 miles of any grid point in Alameda County
* identify the stations that meet Ranson's criteria for inclusion in each year
* calculate the "bias" adjustment for each weather station and for the county
* bin the averaged adjusted temperature data, aggregate it by month using the categories Ranson used

Prerequisites

* install geopy using command pip install geopy
* weather.csv must be in the same directory as ga3.ipynb for it to load properly. Please download weather_data_ca.csv from https://osf.io/qvyw5/ and renamed it to weather.csv


Contents:
* ga3.ipynb : This file contains documentation and codes to meet assignment requirements.
	 
	*  First retrive the weather data from weather.csv and remove the rows related to "TMIN" and merge with stations_within_10miles_alameda.csv which generated in group_assignment2 folder and remove those stations not appeared in stations_within_10miles_alameda.csv file.
	*  Then meet Ransons' criteria by converting all temperatures to Fahrenheit degree.
	* Calculate bias adjustment and use it to adjust temperature.
	 
	*	Eventually, to bin the averaged adjusted maximum temperature in 11 bins (less and equal 10F, 10–20F,…, 90–100F, and large and equal than 100 F)
and and five daily precipitation bins( 0mm, 1–4mm, 5–14 mm, 15–29 mm, and large and equal than 30 mm)

* station_adjusted.csv : This csv file contains all the data after bias adjustment and meets Ranson's criteria.

* ga3.pdf : pdf version of ga3.ipynb

* environment: See stat159.yml in our home directory.
