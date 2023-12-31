#!/usr/bin/python3
""" class Square Module"""


class Square:
    """ class Square"""
    def __init__(self, size=0):
        """ instantializing a new square

        Args:
            value (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """get size.

        Return:
            size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value (int): size of the square.
        """
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """Compute area.

        Return:
            area.
        """
        return self.__size ** 2

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __ge__(self, other):
        return self.size >= other.size
