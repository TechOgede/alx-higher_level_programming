#!/usr/bin/python3
class Node:
    '''Defines the node of a singly linked list'''
    def __init__(self, data, next_node=None):
        '''initialises the node
         Args:
            data (int): +ve or -ve int
            next_node (Node): next node in list or None'''
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        ''' Retrieves data in node'''
        return self.__data

    @data.setter
    def data(self, value):
        ''' Sets the data attribute to value
        Args:
            value (int): denotes the data attr of a Node object '''
        if not isinstance(value, int):
            raise TypeError("next_node must be a Node object")

    @property
    def next_node(self):
        ''' Retrieves the value in the next_node attr'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' Sets the next_node attr of a Node object
        Args:
            value (Node): denotes the value to updatew next_node to '''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    ''' Defines a singly linked list'''
    def __init__(self):
        ''' initialises the list '''
        self.__head = None

    def __str__(self):
        ''' Prints the data attr of every node in a linked list'''
        ptr = self.__head
        string = ""
        while ptr is not None:
            string += str(ptr.data)
            if ptr.next_node is not None:
                string += "\n"
            ptr = ptr.next_node
        return string

    def sorted_insert(self, value):
        ''' Creates a new node at inserts it at the appropriate position
            based on on increasing order of arrangement
        Args:
            value (int): to be used to init the data attr of the new node '''
        node = Node(value)
        ptr = self.__head
        prev = Node(0)
        while ptr is not None:
            if ptr.data > value:
                break
            prev = ptr
            ptr = ptr.next_node
        node.next_node = ptr
        if ptr == self.__head:
            self.__head = node
        else:
            prev.next_node = node
