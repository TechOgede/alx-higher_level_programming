#!/usr/bin/python3
''' This module defines tests for the class, Base '''


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


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

    def test_to_json_string(self):
        ''' Tests the static method, to_json_string '''
        self.assertEqual(Base.to_json_string(None), "[]")
        list_dict = [{'class': 'Base', 'parent': 'object'}]
        self.assertEqual(Base.to_json_string(list_dict), json.dumps(list_dict))

    def test_save_to_file(self):
        ''' Tests the method, save_to_file '''
        list_cls = [Rectangle, Square]
        for cls in list_cls:
            inst_1 = cls(2, 3, id=4)
            inst_2 = cls(4, 5, id=8)

            # check file content when method is called with None
            list_inst = None
            cls.save_to_file(list_inst)
            self.assertTrue(os.path.exists(f'{cls.__name__}.json'))
            with open(f'{cls.__name__}.json', 'r') as f:
                self.assertEqual(Base.to_json_string(list_inst), f.read())

            list_inst = [inst_1, inst_2]
            cls.save_to_file(list_inst)
            list_inst = [inst_1.to_dictionary(), inst_2.to_dictionary()]
            self.assertTrue(os.path.exists(f'{cls.__name__}.json'))
            with open(f'{cls.__name__}.json', 'r') as f:
                self.assertEqual(Base.to_json_string(list_inst), f.read())

    def test_from_json_string(self):
        ''' Tests the static method, from_json_string'''
        list_inst = [True, '5', [3]]
        json_str = Rectangle.to_json_string(list_inst)
        self.assertTrue(type(json_str) is str)
        from_json = Rectangle.from_json_string(json_str)
        self.assertTrue(type(from_json) is list)
        self.assertTrue(list_inst == from_json)
        for obj in from_json:
            self.assertTrue(isinstance(obj, object))
        # for None
        self.assertEqual(Rectangle.from_json_string(None), [])

    def test_create(self):
        ''' Tests the class method, create '''
        inst = Square.create(id=10, size=50, x=4, y=7)
        self.assertTrue(type(inst) is Square)
        self.assertEqual(inst.id, 10)
        self.assertEqual(inst.size, 50)
        self.assertEqual(inst.x, 4)
        self.assertEqual(inst.y, 7)

    def test_load_from_file(self):
        ''' Tests the class method, load_from_file '''
        # delete files from previous test
        os.remove('Rectangle.json')
        os.remove('Square.json')

        # check return value when file doesnt exist
        self.assertFalse(os.path.exists('Rectangle.json'))
        new_insts = Rectangle.load_from_file()
        self.assertTrue(type(new_insts) is list and new_insts == [])

        list_cls = [Rectangle, Square]
        for cls in list_cls:
            inst_1 = cls(2, 3, id=4)
            inst_2 = cls(4, 5, id=8)

            list_inst = [inst_1, inst_2]
            cls.save_to_file(list_inst)
            self.assertTrue(os.path.exists(f'{cls.__name__}.json'))
            new_insts = cls.load_from_file()
            self.assertTrue(type(new_insts) is list)
            self.assertFalse(list_inst is new_insts)
            for obj in new_insts:
                self.assertTrue(isinstance(obj, Base))
