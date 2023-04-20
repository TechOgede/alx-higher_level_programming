#!/usr/bin/python3
''' This module defines test cases for the class, Square '''
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import unittest


class TestSquare(unittest.TestCase):
    ''' This class defines test cases for the class Square '''
    def setUp(self):
        ''' Creates Square instances '''
        self.s1 = Square(2)

    def tearDown(self):
        ''' cleans up '''
        self.s1.decrement()

    def test_square(self):
        ''' Tests instance class etc '''
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(isinstance(self.s1, Square))
        self.assertTrue(isinstance(self.s1, Rectangle))
        self.assertTrue(isinstance(self.s1, Base))

        # check that the value of 'size' is assigned to both width and height
        self.assertEqual(self.s1.width, 2)
        self.assertEqual(self.s1.height, 2)

        # check that no new attrs were created in Square
        self.r1 = Rectangle(1, 2)
        self.assertEqual(len(self.s1.__dict__), len(self.r1.__dict__))

        # check str magic functin
        self.assertEqual(str(self.s1), '[Square] (1) 0/0 - 2')

    def test_size_getter_setter(self):
        ''' Tests the size getter and setter '''
        self.assertEqual(self.s1.size, 2)
        self.s1.size = 6

        self.assertNotEqual(self.s1.size, 2)
        self.assertEqual(self.s1.width, 6)
        self.assertEqual(self.s1.height, 6)

        # check for exception
        with self.assertRaises(TypeError) as e:
            self.s1.size = '8'
        self.assertEqual(str(e.exception), 'width must be an integer')
        with self.assertRaises(ValueError) as e:
            self.s1.size = -1
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test_update(self):
        ''' Tests the update method '''
        self.s1.update(10, 11, 12, 13, size=15)

        self.assertEqual(self.s1.id, 10)
        # check that keyword is skipped
        self.assertEqual(self.s1.size, 11)

        self.assertEqual(self.s1.x, 12)
        self.assertEqual(self.s1.y, 13)

        # check for keyword use alone
        self.s1.update(id=20, size=30, x=40, y=50)
        self.assertEqual(self.s1.id, 20)
        self.assertEqual(self.s1.size, 30)
        self.assertEqual(self.s1.x, 40)
        self.assertEqual(self.s1.y, 50)

    def test_to_dictionary(self):
        '''Tests the to_dictionary method '''
        dict_ = self.s1.to_dictionary()
        self.assertIn('id', dict_)
        self.assertIn('size', dict_)
        self.assertIn('x', dict_)
        self.assertIn('y', dict_)
