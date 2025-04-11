def derivative(xs: list):
    
    return [(i * x) for i, x in enumerate(xs)][1:]





def test():
        assert derivative([0, 1, 2, 3, 4]) == [1, 4, 9, 16]
    assert derivative([1, 0, 5, 3]) == [0, 10, 9]
    assert derivative([3, 2, 1]) == [2, 2]
    assert derivative([10, 0, -5, 3]) == [0, -10, 9]
    assert derivative([]) == []
    assert derivative([0]) == []
    assert derivative([5]) == []
    assert derivative([0, 0, 0]) == [0, 0]
    assert derivative([-1, -2, -3]) == [-2, -6]
    assert derivative([1, 1, 1, 1]) == [1, 2, 3]  # new test case
