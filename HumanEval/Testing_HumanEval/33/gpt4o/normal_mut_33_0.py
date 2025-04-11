def sort_third(l: list):
    
    l = list(l)
    l[::3] = sorted(l[::3])
    return l





def test():
        assert sort_third([3, 1, 2, 6, 5, 4, 9, 8, 7]) == [3, 1, 2, 6, 5, 4, 9, 8, 7]
    assert sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 8, 7, 6, 5, 4, 9, 2, 1]
    assert sort_third([]) == []
    assert sort_third([1, 2, 3]) == [1, 2, 3]
    assert sort_third([1, 3, 5, 2, 4, 6]) == [1, 3, 5, 2, 4, 6]
    assert sort_third([1, 5, 3, 2, 4, 6, 7, 8, 9]) == [1, 5, 3, 2, 4, 6, 7, 8, 9]

METADATA = {}
