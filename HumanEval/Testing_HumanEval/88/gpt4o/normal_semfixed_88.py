def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 


def test():
    # Test case 1: Empty array
    assert sort_array([]) == []
    
    # Test case 2: Array with one element
    assert sort_array([1]) == [1]
    
