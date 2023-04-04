#!/usr/bin/python3
''' this module uses unittest to test the function, max_integer() '''
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax_integer(unittest.TestCase):
    ''' In this class, we use methods from unittest.TestCase to use
         in testing max_integer
    '''
    def test_max_integer(self):
        ''' Method that does the actual testing '''
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([0.5, 1.25, 1.27, 3.44]), 3.44)
        self.assertEqual(max_integer([1, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -4, -2]), -1)
        self.assertEqual(max_integer([1000, 10000, 1000000]), 1000000)
