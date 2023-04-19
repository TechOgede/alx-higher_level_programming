#!/usr/bin/python3
''' This module defines tests for the class, Base '''


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    ''' This class defines test cases for the attrs and methods in Base '''
    def setUp(self):
        ''' Instantiates objects for test '''
        self.b1 = Base()
        self.b2 = Base(12)
        self.b3 = Base()

    def tearDown(self):
        ''' Clean up '''
        self.b1.decrement()
        self.b2.decrement()
        self.b3.decrement()

    def test_base(self):
        ''' Tests for class type and presence of attrs '''
        self.assertTrue(issubclass(Base, object))
        self.assertIs(type(self.b1), Base)
        self.assertIn('_Base__nb_objects', dir(Base))
        self.assertRaises(TypeError, Base, 1, 2, 3)
        self.assertTrue(hasattr(self.b1, 'id'))
        self.assertTrue(type(self.b1.id) is int)
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 12)
        self.assertEqual(self.b3.id, 2)
