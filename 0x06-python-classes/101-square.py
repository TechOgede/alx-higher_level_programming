#!/usr/bin/python3
''' This Module defines a Square class. It has two  private instance
    variables, size and position.'''


class Square:
    ''' This class has one private instance variable'''
    def __init__(self, size=0, position=(0, 0)):
        '''Args:
            size (int): positive integer. Denotes the size of a square.
            position (tuple): consists of 2 +ve integers. Denotes coordinates
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        ''' Getter for the size
        Returns:
          an integer. the size variable'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Setter for the priv var, size
        Args:
          value: value to which size is updated'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        ''' Retrieves the position coordinates
        Returns:
          a tuple bearing the coordinates '''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter for priv var, position
        Args:
          value: value to which position is set'''
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        ''' Calculates the area of the square
            Returns:
              an integer
        '''
        return self.__size * self.__size

    def my_print(self):
        ''' Prints the square using '#' '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end='')
                for k in range(self.__size):
                    print('#', end='')
                print()

    def __str__(self):
        ''' Called automatically when a Square object\
         is passed as arg to print()'''
        string = ""
        if self.__size == 0:
            return string
        else:
            for i in range(self.__position[1]):
                string += "\n"
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    string += " "
                for k in range(self.__size):
                    string += "#"
                string += "\n"
        return string
