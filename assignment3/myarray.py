from ast import If
from msilib.schema import SelfReg
from pydoc import Doc
from itertools import chain
from time import sleep
from turtle import shape
from xmlrpc.client import boolean
from matplotlib import docstring


class Array:
    def __init__(self, shape, *values):
        """
        Initialize an array of 1-dimensionality. Elements can only be of type:
        - int
        - float
        - bool

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.

        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        # Check if the values are of valid type

        # Optional: If not all values are of same type, all are converted to floats.
        # if len(list(values)) > 1:
        self.elements = list(values)
        # elif len(list(values)) == 1:
            # self.elements = values
        self.demention = tuple(shape)
        self.__str__()
        self.__valuetype__()
        self.__shapematch__()

    def __getitem__(self, *item):
        if len(item) == 1:
            return self.elements[item[0]]
        elif len(item) == 2:
            nd =[]
            for i in range(self.demention[0]):
                nd.append(self.elements[self.demention[-1]*i: self.demention[-1]*(i+1)])
            return (nd[item[0]])[item[1]]
        
    # def nd (self):
    #     """ Flattens the N- dimensional array of values into a 1-
    #     dimensional array .
    #     Returns :
    #     list : flat list of array values .
    #     """
    #     nd=[]
    #     for _ in range(len(self.demention[1:])):
    #         nd = list(chain(*nd))
    #         return str(nd)

    def __valuetype__(self):
        """Checks the array input values, and the array input type.
        
        Returns:
            True: if both the array values are in the same data type.
            False: if not True.
        """
        if type(self.elements) == list:
            for i in range(len(self.elements)):
                if type(self.elements[i]) in [int, float, bool]:
                    if i < len(self.elements) - 1:
                        if type(self.elements[i]) == type(self.elements[i + 1]):
                            return True
                        else:
                            raise ValueError('Values are not the same type.')
                    else:
                        raise ValueError('Values are not the same type.')
                else:
                    return False
        elif type(self.elements) != list:
            if type(self.elements) in [int, float, bool]:
                return True
            else:
                return False

    def __shapematch__(self):
        """Checks the demention of the array with the amount of values.
        
        Returns:
            True: if demention values matches the amount of values.
            False: if not True.
        """
        size = 1
        for i in range(len(self.demention)):
            if self.__valuetype__():
                size = size * self.demention[i]
                if size == len(self.elements):
                    return True
            else:
                raise ValueError(
                'The shape does not match the amount of the input values.')            

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        # for i in range(len(self.vlaues)):
        #     self.values.append(self.values[i])
        if len(self.demention) == 1:
            return str(self.elements)
        # elif len(self.demention) > 1:
        elif len(self.demention) == 2:
            nd =[]
            for i in range(self.demention[0]):
                nd.append(self.elements[self.demention[-1]*i: self.demention[-1]*(i+1)])
            return str(nd)
        elif len(self.demention)>2:
            nd=[]
            for i in range(len(self.demention[0])):
                nd.append(self.elements[self.demention[1:]])
            return str(nd)

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        # new_a = Array(other)
        new_a = []
        if self.__valuetype__():
            if type(other) == list:
                for i in range(len(self.elements)):
                    new_a.append(self.elements[i] + other[i])
            elif type(other) in [int, float]:
                for i in range(len(self.elements)):
                    new_a.append(self.elements[i] + other)
            return new_a
        elif not self.__shapematch__() or not self.__valuetype__():
            return "NotImplemented!"

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        new_a = []
        if self.__valuetype__():
            if type(other) == list:
                for i in range(len(self.elements)):
                    new_a.append(self.elements[i] - other[i])
            elif type(other) in [int, float]:
                for i in range(len(self.elements)):
                    new_a.append(self.elements[i] - other)
            return new_a
        elif not self.__shapematch__() or not self.__valuetype__():
            return "NotImplemented!"

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        # shapematch is not need.
        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        new_a = []
        if self.__valuetype__():
            if type(other) == list:
                for i in range(len(self.elements)):
                    new_a.append(self.elements[i] * other[i])
            elif type(other) in [int, float]:
                for i in range(len(self.elements)):
                    new_a.append(self.elements[i] * other)
            return new_a
        elif not self.__shapematch__() or not self.__valuetype__():
            return "NotImplemented!"

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        eq=False
        if type(other) != list:
            return False

        # elif type(other) == list:
        #     # tyother = lambda x: (type(x[i]) == type(x[i+1]) for i in range(len(x)-1))
            
        #     if self.__valuetype__():
        #         if len(self.elements) == len(other):
        #             return True
        elif type(other) == list:
            if len(self.elements) != len(other):
                return False
            elif len(self.elements) == len(other):
                for i in range(len(self.elements)):
                    if type(self.elements[i]) == type(other[i]):
                        eq = True
                    elif type(self.elements[i]) != type(other[i]):
                        eq = False
                        break
                return eq
            elif type(other) != (int or float or bool):
                return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
            Or if `other` is a number, it returns True where the array is equal to the number and False
            where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """
        if type(other) != list:
            if type(other) in [int, float, bool]:
                return 'Valid value type.'
            else:
                raise TypeError('The values of the array is not correct, \
                    it should be at either an int or float or boolean type.')
        equal = []
        if type(other) == list:
            if len(self.elements) != len(other):
                raise ValueError('Shapes of the 2 arrays do not match.')
            elif len(self.elements) == len(other):
                for i in range(len(self.elements)):
                    if self.elements[i] == other[i]:
                        equal.append(True)
                    elif not self.elements[i] == other[i]:
                        equal.append(False)
                return equal
            else:
                print('Length of the array do not match!')

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """
        for i in range(len(self.elements)):
            if type(self.elements[i]) in [int, float]:
                return float(min(self.elements))
            else:
                print('Value type should be either int or float.')
