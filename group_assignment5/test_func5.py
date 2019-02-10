import pandas as pd 
import numpy as np 
import unittest
from func5 import *

class utest(unittest.TestCase):
    """ unit test class

    """
    def test_get_stat(self):
    	"""
    	test if the get_stat function return the correct number
    	"""

    	self.assertEqual(get_stat(df1, df2).values.tolist(), [[9], [57], [22]])
        
    def test_find_p_value(self):
    	"""
    	test if the find_p_value function return the correct number
    	"""
    	self.assertEqual(find_p_value(df1), [1.0, 1.0, 0.6666666666666666])

    def test_fisher_comb(self):
    	"""
    	test if the fisher_comb function return the correct number
    	"""
    	self.assertAlmostEqual(fisher_comb(find_p_value(df1)), 0.8109302162163289)

if __name__ == '__main__':
    unittest.main()