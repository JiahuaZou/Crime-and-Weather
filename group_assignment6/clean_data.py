import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
import re

def get_filenames(start_year = 1980, end_year = 2009, path = 'ucr_offenses_known_monthly_1960_2016_dta/'):
    """function that selects .dta files within needed time range
    Args:
        start_year: start year of weather data, 1980
        end_year: end year of weather data, 2009
        path: path of folder that contains all crime data
    Returns:
        all dta files within time range 1980-2009
    """
    filenames = []
    for filename in os.listdir(path):
        #ignore pdf files in folder, filter out dta file names that contain 1980-2009
        if filename.endswith('.dta'):
            for years in range(start_year, end_year + 1):
                if str(years) in filename:
                    filenames.append(filename)
    return(filenames)

def get_clean_data(path = 'ucr_offenses_known_monthly_1960_2016_dta/', 
    identifier_variables = ['fips_state_county_code', 'state', 'date', 'year', 'zip_code', 'month'], 
    crime_category = ['act_aggravated_assault', 'act_simple_assault', 'act_murder', 'act_robbery_total', 
    'act_manslaughter', 'act_theft_total', 'act_mtr_vhc_theft_total', 'act_burglary_total', 'act_rape_total'], 
    start_year = 1980, end_year = 2009, selected_area = 'all'):
    """function that filters out needed variables, aggregates crime data for each category, splits crime data for East 
       and West Alameda, and output useful data into csv files
    Args:
        identifier_variables: variables that contain time and location information for crime data
        crime_category: variables that contain total amount of crimes happended in each category
    Returns:
        Three csv files that contain appropriate crime data needed for Poisson and permutation for Alameda, 
        West Alameda and East Alameda, respectively
    """
    all_df = []
    for i in get_filenames(start_year, end_year):
        file = path + i
        print(file)
        each_df = pd.read_stata(file)
        each_df = each_df[identifier_variables + crime_category]
        each_df = each_df[each_df['fips_state_county_code'] == '06001']
        each_df['zipcode'] = each_df['zip_code'].apply(lambda x: str(x)[0:5])
        #split Alameda into West and East Alameda according to zip code
        if selected_area == 'east':
            each_df = each_df[(each_df['zipcode'] == '94550') | (each_df['zipcode'] == '94566') | 
                              (each_df['zipcode'] == '94586') | (each_df['zipcode'] == '94568') | 
                              (each_df['zipcode'] == '94588') | (each_df['zipcode'] == '94551')]
        elif selected_area == 'west':
            each_df = each_df[(each_df['zipcode'] != '94550') & (each_df['zipcode'] != '94566') & 
                     (each_df['zipcode'] != '94586') & (each_df['zipcode'] != '94568') & 
                     (each_df['zipcode'] != '94588') & (each_df['zipcode'] != '94551') &
                     (each_df['zipcode'] != '0') & (each_df['zipcode'] != '0.0') & 
                     (each_df['zipcode'] != 'not r') & (each_df['zipcode'] != 'missi')]
        each_df.loc[:, 'YearMonth'] = [int(re.sub('-', '', date)[0:6]) for date in each_df.loc[:, 'date']]
        #sum up amount of crimes taken place in each category for each month
        each_df = each_df.groupby(['YearMonth'])[crime_category].sum()
        each_df['crime_sum'] = each_df.sum(axis = 1)
        each_df = each_df['crime_sum'].reset_index()
        all_df.append(each_df)
    df = pd.concat(all_df).fillna(0)
    df = df.sort_values('YearMonth').reset_index()
    #split variable 'YearMonth" into two variables 'year' and "month' for Poission regression
    del df['index']
    df['year'] = df['YearMonth'].apply(lambda x: str(x)[:4])
    df['month'] = df['YearMonth'].apply(lambda x: str(x)[4:])
    if selected_area == 'east':
        df.to_csv('east_alameda_crime.csv')
    elif selected_area == 'west':
        df.to_csv('west_alameda_crime.csv')
    else:
        df.to_csv('all_alameda_crime.csv')
    return(df)
