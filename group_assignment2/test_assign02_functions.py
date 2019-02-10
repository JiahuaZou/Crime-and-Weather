#test_assign02_functions.py


import Assignment_2_Functions as a2
import pandas as pd
from geopy import distance
import geopy


#Three test functions to test three functions in Assignment_2_Functions.py file.



def test_within_alameda():
  ''' 
    This function test within_alameda function with all cases.
    First, read a grid points in Alameda csv file to create a pandas data frame.
    let x equals to 10, and find data from the stations_within_10miles_alameda.csv
    Then, test two situations with two cases return True and one case return False.
  '''

  data = pd.read_csv("grid_points_alameda.csv")
  x = 10
  lat=[37.8123, 37.7075,41.9869]
  lon=[-122.21600000000001,-122.0687,-123.7185]
  alameda=[(37.90436,-122.272787)]

  assert a2.within_alameda(x,lat[0],lon[0], data)==True
  assert a2.within_alameda(x,lat[1],lon[1], data)==True
  assert a2.within_alameda(x,lat[2],lon[2], data)== False

def test_find_optimal():
    ''''This function test find_optimal function with all cases.
        We need to test both optimal1 and optimal2 with starting point(37.905098, -122.272225).
        Check whether optimal1 and optimal2 satisfies the condition the subtraction is less than 0.00005.
    '''
    i1 = a2.find_optimal(37.905098, -122.272225, 5)[0]
    i2 = a2.find_optimal(37.905098, -122.272225, 5)[1]
    assert distance.distance((37.905098, -122.272225), (37.905098-i1, -122.272225-i1)).miles - 5 < 0.00005
    assert distance.distance((37.905098, -122.272225), (37.905098, -122.272225-i2)).miles - 5 < 0.00005




def test_idwa():
  '''
    This function idwa function with all cases.
    There are two situations : if the latitude and longtitude of the weather station are
    coincide with one of the grid points, the inverse distance with that grid point would be 1/0.00001self.
    Otherwise, the inverse distance is 1/distance between weather station and grid point.
    First three assert statements tests the second situationself.
    Last three assert statements test the first situation.
  '''

  loc1= [(41.49008, -71.312796), (-41.32, 174.81)]
  loc2= [(41.499498, -81.695391), (40.96, -5.50),(38.7890,-41.20),(37.6425,174.84)]
  loc3= [(41.499498, -81.695391), (40.96, -5.50),(38.7890,-41.20),(37.6425,174.84),(-41.32, 174.81)]
  helper1 = []
  helper2 = []
  helper1.append(loc1[0])
  helper2.append(loc1[1])
  
  assert a2.idwa(loc1,loc2) == [0.0007405144831780838, 0.00011894394959055386 ]
  assert a2.idwa(helper1,loc2)== [0.0007405144831780838]
  assert a2.idwa(helper2,loc2)== [0.00011894394959055386]
  assert a2.idwa(loc1,loc3)== [0.0006144053474114974, 20000.000095155156]
  assert a2.idwa(helper1,loc3)== [0.0006144053474114974]
  assert a2.idwa(helper2,loc3)== [20000.000095155156]
