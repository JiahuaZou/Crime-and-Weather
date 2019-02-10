import unittest
from func1 import *

class utest(unittest.TestCase):
    
    def test_idwa(self):
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
      
        self.assertAlmostEqual(idwa(loc1,loc2), [0.0007405144831780838, 0.00011894394959055386 ])
        self.assertAlmostEqual(idwa(helper1,loc2), [0.0007405144831780838])
        self.assertAlmostEqual(idwa(helper2,loc2), [0.00011894394959055386])
        self.assertAlmostEqual(idwa(loc1,loc3), [0.0006144053474114974, 20000.000095155156])
        self.assertAlmostEqual(idwa(helper1,loc3), [0.0006144053474114974])
        self.assertAlmostEqual(idwa(helper2,loc3), [20000.000095155156])
        
if __name__ == '__main__':
    unittest.main()
