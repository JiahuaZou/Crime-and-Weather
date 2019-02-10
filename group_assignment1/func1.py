#!/usr/bin/env python
# coding: utf-8

# In[1]:


#since conda parkage does not include geopy, our environment file does not include geopy. Please check if you have installed geopy or not before runnig the code below. If you haven't, run "pip install geopy" at your local terminal.


# In[ ]:


#import the libraries.
from geopy import distance
import geopy
import numpy as np

# In[17]:


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








