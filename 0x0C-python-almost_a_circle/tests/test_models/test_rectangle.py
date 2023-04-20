#!/usr/bin/python3
''' This module defines tests for the class, Rectangle '''


import unittest
from models.base import Base
from models.rectangle import Rectangle
import sys
import io


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

    def test_area(self):
        ''' tests the area method '''
        self.assertEqual(self.r1.area(), 8)

    def test_display(self):
        ''' tests the display method '''
        buf = io.StringIO()
        sys.stdout = buf
        self.r1.display()
        self.assertEqual(buf.getvalue(), '##\n##\n##\n##\n')
        # checking that x and y are handled
        buf.seek(0)
        buf.write("")
        buf.seek(0)
        self.r2.display()
        self.assertEqual(buf.getvalue(),
                         '\n  ###\n  ###\n  ###\n  ###\n  ###\n  ###\n')

    def test_str(self):
        ''' tests the str output '''
        str_ = str(self.r1)
        self.assertEqual(str_, '[Rectangle] (1) 0/0 - 2/4')

    def test_update(self):
        ''' Tests the update method '''
        self.r1.update(4, 5, 10, 3, 6)
        self.assertEqual(self.r1.id, 4)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 6)

        # passing keyword args
        self.r1.update(id=10, width=4, height=5, x=5, y=4)
        self.assertEqual(self.r1.id, 10)
        self.assertEqual(self.r1.width, 4)
        self.assertEqual(self.r1.height, 5)
        self.assertEqual(self.r1.x, 5)
        self.assertEqual(self.r1.y, 4)

    def test_to_dictionary(self):
        '''Tests the to_dictionary method '''
        dict_ = self.r1.to_dictionary()
        self.assertIn('id', dict_)
        self.assertIn('width', dict_)
        self.assertIn('height', dict_)
        self.assertIn('x', dict_)
        self.assertIn('y', dict_)
