#!/usr/bin/env python
# coding: utf-8

# In[1]:
import geopy
import numpy as np
import pandas as pd


def find_optimal(lat, lon, y):
    """ Function that takes a collection of values at (lat, long) pair of original point, 
        finds the amount to be subtracted from latitude and longitude to obtain a grid point
        y miles away from the initial grid point.
        
     Args:
        lat: latitude of original weather station 
        lon: longitude of original weather station
        y: distance away from the initial grid point
        
    Returns:
        optimal1: The amount to be subtracted from both latitude and longitude from initial grid point 
        to obtain a grid point 5 miles away on south-east direction
        optimal2: The amount to be subtracted from longitude from initial grid point to obtain a grid 
        point 5 miles away on east direction. 
    """
    optimal1 = 0
    optimal2 = 0
    for i in np.linspace(0, 1, 1200):
        if geopy.distance.distance((lat, lon), (lat - i, lon - i)).miles - y < 0.00005:
            optimal1 = i
        if geopy.distance.distance((lat, lon), (lat, lon - i)).miles - y < 0.00005:
            optimal2 = i
    return((optimal1, optimal2))


# In[2]:


def within_alameda(x, lat, lon, alameda):
    """ Function that takes a collection of values at (lat, long) pair of a point, and a distance
        of x miles, and a list of grid points in Alameda, and returns weather the point is within x miles of Alameda.
    
    Args:
      x: miles
      lat: latitude of the weather station
      lon: longitude of the weather station
      alameda: a list of grid points we overlay on Alameda
      
    Returns: True if the point is within x miles of Alameda, false if the point is not within x miles of Alameda.
    """
    within = False
    for i, j in zip(alameda.lat, alameda.lon):
        if geopy.distance.distance((i, j), (lat, lon)).miles <= x:
            return within or True
    return within


# In[3]:


def idwa(loc1, loc2):
    """ Function that takes a collection of values at (lat, long) pairs (intended to represent weather stations) and 
        finds the weighted average inverse distance to another given set of (lat, long) points 
        (intended to represent grid points within a county). 
        define 1st location as weather station, 2nd location as grid points within a county.

    Args:
        loc1: A list of tuples that contains the latitude and longtitude of the weather stations that are within 50 miles of the county.
        loc2: A list of tuples that contains the latitude and longtitude of all the grid points in a county.
        
    Returns:
         A list of inverse-distance weighted average values.

    """
    weighted_average_inverse_distance = []
    for l1 in loc1:
        dist = [geopy.distance.distance(l1, l2).miles for l2 in loc2]
        inv_dist = [1/x if x != 0 else 1/(0.00001+x) for x in dist]
        weighted_average_inverse_distance.append(np.mean(inv_dist))
  
    return weighted_average_inverse_distance

