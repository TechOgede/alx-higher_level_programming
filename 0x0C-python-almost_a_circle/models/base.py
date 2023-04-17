#!/usr/bin/python3
''' This module defines a class, Base. '''

import json
import csv


class Base:
    ''' Serves as the base class for other classes in this project '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def decrement(self):
        ''' Reduces the value of __nb_objects by 1
            In a sense, it 'deletes' the instance '''
        if Base.__nb_objects:
            Base.__nb_objects -= 1

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON rep of list_dictionaries '''
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return json.dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes the JSON rep of a a list of instances to a file
            Args:
                list_objs: list of instances that inherit Base
        '''
        list_dict = []
        if list_objs:
            for obj in list_objs:
                dict_ = obj.to_dictionary()
                list_dict.append(dict_)

        str_to_write = Base.to_json_string(list_dict)
        with open(f'{cls.__name__}.json',
                  "w", encoding='utf-8') as f:
            f.write(str_to_write)

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the Python object represented by a Json string'''
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        ''' Returns an instance with all attributes already set '''
        if 'size' in dictionary:
            inst = cls(1)
        else:
            inst = cls(1, 2)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        ''' Returns a list of instances '''
        inst_list = []
        try:
            f = open(f'{cls.__name__}.json', "r", encoding='utf-8')
        except FileNotFoundError:
            pass
        else:
            dict_list = cls.from_json_string(f.read())
            for dict_ in dict_list:
                inst_list.append(cls.create(**dict_))
        finally:
            f.close()
            return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' Writes the CSV rep of a a list of instances to a file
            Args:
                list_objs: list of instances that inherit Base
        '''
        list_csv = []
        if list_objs:
            for obj in list_objs:
                csv_ = obj.to_csv()
                list_csv.append(csv_)

        with open(f'{cls.__name__}.csv',
                  "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(list_csv)

    @classmethod
    def create_from_csv(cls, *list_):
        from models.rectangle import Rectangle
        from models.square import Square
        ''' Creates an object from its CSV representation'''
        if len(list_) == 5:
            inst = Rectangle(1, 2)
        else:
            inst = Square(3, 4)
        inst.update(*list_)

        return inst

    @classmethod
    def load_from_file_csv(cls):
        ''' Deserializes csv data from a file '''
        list_inst = []
        try:
            f = open(f'{cls.__name__}.csv', "r", newline="")
        except FileNotFoundError:
            pass
        else:
            reader = csv.reader(f)
            for row in reader:
                inst = cls.create_from_csv(*row)
                list_inst.append(inst)
            print('bulaba3')
        finally:
            f.close()
            return list_inst
