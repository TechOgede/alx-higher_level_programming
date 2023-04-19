#!/usr/bin/python3
''' This module defines tests for the class, Rectangle '''


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    ''' Test cases for Rectangle '''
    def setUp(self):
        ''' Instantiates objects for each test case '''
        self.r1 = Rectangle(2, 4)
        self.r2 = Rectangle(3, 6, 2, 1, 3)
        self.r3 = Rectangle(4, 8)

    def tearDown(self):
        ''' deletes instances created in setUp'''
        self.r1.decrement()
        self.r2.decrement()
        self.r3.decrement()

    def test_rectangle_attrs(self):
        ''' Test cases '''
        self.assertTrue(issubclass(Rectangle, object))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(type(self.r1) is Rectangle)
        self.assertTrue(isinstance(self.r1, Base))

        # check for attributes in instance
        self.assertIn('_Rectangle__width', self.r1.__dict__)
        self.assertIn('_Rectangle__height', self.r1.__dict__)
        self.assertIn('_Rectangle__x', self.r1.__dict__)
        self.assertIn('_Rectangle__y', self.r1.__dict__)
        self.assertIn('id', self.r1.__dict__)

        # check for properties
        self.assertIn('x', Rectangle.__dict__)
        self.assertIn('y', Rectangle.__dict__)
        self.assertIn('width', Rectangle.__dict__)
        self.assertIn('height', Rectangle.__dict__)

        # check that each value is assigned to the apropriate attr
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.width, 3)
        self.assertEqual(self.r2.height, 6)
        self.assertEqual(self.r2.x, 2)
        self.assertEqual(self.r2.y, 1)
        self.assertEqual(self.r2.id, 3)

    # check that setters work as they should
    def test_setters(self):
        ''' Tests setters '''
        self.r2.width = 5
        self.r2.height = 10
        self.r2.x = 4
        self.r2.y = 5
        self.assertNotEqual(self.r2.width, 3)
        self.assertNotEqual(self.r2.height, 6)
        self.assertNotEqual(self.r2.x, 2)
        self.assertNotEqual(self.r2.y, 1)

    # check that defensive code works
    def test_exceptions(self):
        ''' checks for exceptions and appropraite messages '''
        with self.assertRaises(TypeError) as e:
            self.r2.width = True
        self.assertEqual(str(e.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as e:
            self.r2.height = False
        self.assertEqual(str(e.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as e:
            self.r2.x = 'x'
        self.assertEqual(str(e.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as e:
            self.r2.y = 'y'
        self.assertEqual(str(e.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as e:
            self.r2.width = 0
        self.assertEqual(str(e.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as e:
            self.r2.height = 0
        self.assertEqual(str(e.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as e:
            self.r2.x = -1
        self.assertEqual(str(e.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as e:
            self.r2.y = -1
        self.assertEqual(str(e.exception), 'y must be >= 0')
