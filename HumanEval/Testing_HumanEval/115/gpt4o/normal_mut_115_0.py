def max_fill(grid, capacity):
    import math
    
    return sum([math.ceil(sum(arr)/capacity) for arr in grid])



def test():
        assert max_fill([[10, 20, 30], [40, 50, 60]], 50) == 5
    assert max_fill([[5, 10, 15], [20, 25, 30]], 40) == 3
    assert max_fill([[1, 2, 3], [4, 5, 6]], 5) == 3
    assert max_fill([[100, 200], [300, 400]], 250) == 5
    assert max_fill([[0, 0, 0], [0, 0, 0]], 10) == 0

# new test case to detect the fault
def test_with_fault():
    assert max_fill([[1, 1, 1], [1, 1, 1]], 2) == 3  # previously failed test case due to multiplication instead of division

test()
test_with_fault()
