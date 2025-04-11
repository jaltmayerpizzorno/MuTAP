def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 



def test():

    # Test case 1: Empty array
    assert sort_array([]) == []
    
    # Test case 2: Array with one element
    assert sort_array([1]) == [1]
    
    assert sort_array([]) == []
    assert sort_array([1]) == [1]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([1, 4, 3, 0, 2, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 2, 4, 4]) == [4, 4, 2, 2]
    assert sort_array([1, 5, 3, 3]) == [1, 3, 3, 5]

    assert sort_array([]) == []
    assert sort_array([1]) == [1]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    assert sort_array([]) == []
    assert sort_array([1]) == [1]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

    assert sort_array([]) == []
    assert sort_array([1]) == [1]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([-2, 4, 3, 0, 1, 5, -4]) == [5, 4, 3, 1, 0, -2, -4]
    assert sort_array([-2, 4, 3, 0, 1, 5, -3]) == [-3, -2, 0, 1, 3, 4, 5]

    assert sort_array([]) == []
    assert sort_array([1]) == [1]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 2]) == [2, 2]
    assert sort_array([2, 3]) == [2, 3]
    assert sort_array([-2, -4, -3, -1]) == [-1, -2, -3, -4]
    assert sort_array([-2, -3, -4, -1]) == [-4, -3, -2, -1]

    assert sort_array([]) == []
    assert sort_array([1]) == [1]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 2]) == [2, 2]
    assert sort_array([1, 1]) == [1, 1]
    assert sort_array([-3, -2, -1]) == [-3, -2, -1]  # sum of -3 and -1 is even, so descending order
    assert sort_array([-1, 0, 1]) == [-1, 0, 1]  # sum of -1 and 1 is even, so descending order

