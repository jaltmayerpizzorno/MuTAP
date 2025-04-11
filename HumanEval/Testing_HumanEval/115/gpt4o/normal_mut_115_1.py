def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])



def test():
        assert max_fill([[10, 20, 30], [40, 50, 60]], 50) == 5
    assert max_fill([[5, 10, 15], [20, 25, 30]], 40) == 3
    assert max_fill([[1, 2, 3], [4, 5, 6]], 5) == 5
    assert max_fill([[100, 200], [300, 400]], 250) == 5
    assert max_fill([[0, 0, 0], [0, 0, 0]], 10) == 0
    assert max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 3) == 3
    assert max_fill([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 2) == 9
