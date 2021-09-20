
# README.md Assignment3

## Task 3.1

### Prerequisites

This is a python code piece, python version is 3.9.7.
In myarray.py, packages as below listed should be installed:
from ast import If
from msilib.schema import SelfReg
from pydoc import Doc
from itertools import chain
from time import sleep
from turtle import shape
from xmlrpc.client import boolean
from matplotlib import docstring

### Functionality

```python
shape = (4 ,)
# define my_array
my_array = Array (shape , 2, 3, 1, 0)
# __getitem__ should be implemented correctly .
assert my_array[2] == 1
# Printing the array prints the array values nicely .
# For example : [2, 3, 1, 0]
print ( my_array )
```

### Missing Functionality

The current implements are not able to handle nD arrays.

### Usage

It can be used to perform basic methmetics, __add__ , __sub__ , __mul__ , __radd__ , __rsub__ and __rmul__ , you want to check if the argument is a scalar or an array with the same shape. If it is something else you can return NotImplemented.
The r methods The methods radd , rsub and rmul are called to implement the arithmetic operations add , sub , mul with swapped 2 operands. The r methods are only called, if the left (first) operand does not support the operation provided and the operands are of different type. For example, imagine we have an array

```python
1 array1 = Array ((6 ,) , 1, 2, 3, 4, 5, 6)
```

and want to evaluate 10 + array1, where array1 is an instance of our Array
class, which has a radd () method. Python first calls 10.__add (array1). Since 10 (int or foat) does not support the instance of the

Array class, 10__add (array1) it returns NotImplemented. The r-method

```python
array1_ radd (10) is then called.
array1 = Array ((6 ,) , 1, 2, 3, 4, 5, 6)
i = 10
i. __add__ ( array1 ) # Returns NotImplemented

array1 . __radd__ (i) # Returns Array ((6 ,) , 11, 12, 13, 14, 15, 16)
```

## Task 3.2

test_myarray.py contains the functionality to test out the below listed functionalites:

* Check that the print function returns the nice string
* One or more tests verifying that adding to a 1d-array element-wise returns what it's supposed to.
* One or more tests verifying that substracting from a 1d-array element-wise returns what it's supposed to.
* One or more tests verifying that multiplying a 1d-array element-wise by a factor or other 1-d array returns what it's supposed to.
* One or more tests verifying that comparing arrays (by ==) returns what it is supposed to - which should be a boolean.
* One or more tests verifying that comparing a 1d-array element-wise to another array through is equal returns what it's supposed to - which should be a boolean array.
* One or more tests verifying that the the element returned by min element is the "smallest" one in the array.
