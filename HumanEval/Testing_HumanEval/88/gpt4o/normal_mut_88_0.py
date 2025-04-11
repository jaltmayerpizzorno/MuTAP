def sort_array(array):
    
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 



def test():
        # Test case 1: Empty array
    assert sort_array([]) == []

    # Test case 2: Array with one element
    assert sort_array([1]) == [1]

    # Test case 3: Array with even sum of first and last elements
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

    # Test case 4: Array with odd sum of first and last elements
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # Test case 5: Array with even sum and identical elements
    assert sort_array([2, 2]) == [2, 2]

    # Test case 6: Array with odd sum and identical elements
    assert sort_array([1, 1]) == [1, 1]

    # Test case 7: Array with negative elements
    assert sort_array([-3, -2, -1]) == [-3, -2, -1]  # sum of -3 and -1 is even, so descending order

    # Test case 8: Array with mixed positive and negative elements
    assert sort_array([-1, 0, 1]) == [-1, 0, 1]  # sum of -1 and 1 is even, so descending order
