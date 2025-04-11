def sort_array(arr):
    
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


def test():
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 4, 8, 3, 5, 6, 7]
    assert sort_array([10, 3, 15, 7, 8]) == [8, 3, 10, 7, 15]
    assert sort_array([0, 1, 2, 3, 4, 5, 6, 7]) == [0, 1, 2, 4, 3, 5, 6, 7]
    assert sort_array([9, 14, 3, 11, 16]) == [16, 3, 9, 11, 14]
    assert sort_array([]) == []
