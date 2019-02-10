# Crime-and-Weather

# cwcc-g3
RocketGirls101

Group numbers: Jiahua Zou, Yijun Xu, Yikang Li, Jiajing Li, Luyun Lin

## group presentation:

Order of the presentation:

Jiahua Zou: Introduction and Group assignment 1 & 2  
Yijun Xu: Group Assignment 3  
Luyun Lin: Group Assignment 4  
Yikang Li: Group Assignment 5  
Jiajing Li: Group Assignment 6 and conclusion  

Our group presentation video is too large to upload to github. So we post it on Youtube and google drive. Here are two ways you can access it:

Youtube link: https://youtu.be/903q_dOcDOg  

Google drive link (access with @berkeley account): 
https://drive.google.com/file/d/1GadaUY8C6C1MknrX9nnK-xlv-yE3UoWO/view?usp=sharing


## project description
In this project, we access the analysis methods in Ransonâs "Crime, weather, and climate change" paper. Ranson claims that thereâs a correlation between weather and crime rate. However, based on our analysis of Alameda county with the same method as he described, we believe that Ransonâs methods are not acadquate and conclusions might not be reproducible.

In assignment 1, we wrote a function that calculates the distance from two grid points the same way as Ranson did.

In assignment 2, we calculated all stations within 10 miles of Alameda, whereas Ranson calculated all stations within 50 miles of U.S.

In assignment 3, we convert TMAX and PCRP to correct measurement units, bias-corrected the TMAX and PRCP with the same method as Ranson to avoid bias caused by missing data points. After that we bin the TMAX and PRCP based on the same categories as Ranson.

In assignment 4, we first divide the Alameda county in to east and west two parts for future analysis. And Then repeat what weâve done in 3 on these two parts of Alameda.

In assignment 5, we tested whether the weather in Berkeley and Livermore are from the same distribution by doing a Permutation test. It shows that the weather in Berkeley and Livermore is different. Therefore, the way Ranson averaged the weather data thought all counties in U.S. is problematic. 

In assignment 6, we first fitted the poisson model the same way as Ranson did. After that we tested whether east and west Alameda are consistent with a single model by doing a Permutation test. It is shown that the relationship between weather and crime of east and west Alameda is indeed different. 


Considering that in assignment 5 we found weather in two cities within same county is different, in assignment 6 we further conclude that different parts of county's weather might affect crime rate differently, we believe that by obtaining inverse distance average weather for a whole county, this averaged number loses its original meaning, and we can not assume that Ranson's model of effects of climate change on future criminal activity is correct. 

## Data Sources

- weather data: weather_data_ca.csv from https://osf.io/qvyw5/ (downloaded and renamed to weather.csv for our project use)

- crime data: https://www.openicpsr.org/openicpsr/project/100707/version/V7/view These data have already been cleaned (by Jacob Kaplan, a Ph.D. student in Criminology at U. Pennsylvania); his cleaning scripts are here: https://github.com/jacobkap/crime_data
