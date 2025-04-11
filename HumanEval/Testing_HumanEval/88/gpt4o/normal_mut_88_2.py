def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 



def test():
        # Test case 1: Empty array
    assert sort_array([]) == []

    # Test case 2: Array with one element
    assert sort_array([1]) == [1]
    
    # Test case 3: Array with even sum of first and last element
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    
    # Test case 4: Array with odd sum of first and last element
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
