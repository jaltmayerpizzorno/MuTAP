def get_positive(l: list):
    
    return [e for e in l if e > 0]





def test():
        assert get_positive([1, -2, 3, 0, -5, 6]) == [1, 3, 6]
    assert get_positive([-1, -2, -3, -4]) == []
    assert get_positive([0, 0, 0]) == []
    assert get_positive([5, 10, 15]) == [5, 10, 15]
    assert get_positive([]) == []
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

test()
