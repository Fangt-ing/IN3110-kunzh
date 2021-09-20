import unittest
import pytest

import myarray

class TestArray(unittest.TestCase):
    
    def test_str(self):
        # Test if the array print
        
        shape = (4,)
        my_aaray = myarray.Array(shape, 2, 3, 1, 0)
        assert my_aaray[2] == 1
        print(my_aaray)
        # pytest.raises(ValueError, print(my_aaray), [2, 3, 1, 0])
        
        
        assert myarray.Array((3,), 4, 7, 2) == [4, 7, 2]
        AssertionError(ValueError, myarray.Array((3,), 4, 7, 2), [4, 7])
        
        assert myarray.Array((4,), 4, 7, 2, 'm') == [4, 7, 2, 'm']
        AssertionError(ValueError, ((4,), 4, 7, 'm'), [4, 7, 2, 'm'])
        
        assert myarray.Array((2,2), 4, 7, 2, 5) == [4, 7, 2, 5]
        AssertionError(ValueError, myarray.Array((2,2), 4, 7, 2), [4, 7, 2])
        
    def test_sub(self):
        a1 = 1
        assert myarray.Array((3,), 4, 7, 2) - a1 == [3, 6, 1]
        AssertionError(ValueError, myarray.Array((3,), 4, 7, 2) - a1, [1, 4, 1])
        a2 = [1, 3, 4]
        assert myarray.Array((3,), 4, 7, 2) - a2 == [3, 4, -2]
        AssertionError(ValueError, myarray.Array((3,), 4, 7, 2) - a2, [1, 4, 1])
        
    def test_mul(self):
        a1 = 1
        assert myarray.Array((3,), 4, 7, 2) * a1 == [4, 7, 2]
        AssertionError(ValueError, myarray.Array((3,), 4, 7, 2) * a1, [1, 4, 1])
        a2 = [1, 3, 4]
        assert myarray.Array((3,), 4, 7, 2) * a2 == [4, 21, 8]
        AssertionError(ValueError, myarray.Array((3,), 4, 7, 2) * a2, [1, 4, 1])
    
    def test_eq(self):
        a=myarray.Array((3,), 4, 7, 2)
        assert a.__eq__([4, 7, 1]) == True
        assert a.__eq__([4, 7, False]) == False
        assert a.__eq__([True, False, False]) == False
        
    def test_is_equal(self):
        a=myarray.Array((3,), 4, 7, 2)
        assert a.is_equal([4, 7, 2]) == [True, True, True]
        assert a.is_equal([4, 7, 1]) == [True, True, False]
        assert a.is_equal([1, 0, 1]) == [False, False, False]
    
    def test_min_element(self):
        a=myarray.Array((5,), 1, 2 , 3, 4 , 5)
        assert a.min_element() == 1
        AssertionError(ValueError, a.min_element(), 3)
        a=myarray.Array((4,), 2.3, 4.5, 1.9, 3.2)
        assert a.min_element() == 1.9
        AssertionError(ValueError, a.min_element(), 2.3)