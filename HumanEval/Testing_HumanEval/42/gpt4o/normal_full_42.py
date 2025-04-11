def incr_list(l: list):
    
    return [(e + 1) for e in l]





def test():

    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([-1, 0, 1]) == [0, 1, 2]
    assert incr_list([]) == []
    assert incr_list([10, 20, 30]) == [11, 21, 31]
    assert incr_list([0]) == [1]
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([-1, 0, 1]) == [0, 1, 2]
    assert incr_list([]) == []
    assert incr_list([10, 20, 30]) == [11, 21, 31]
    assert incr_list([0]) == [1]
    assert incr_list([2, 3, 4]) == [3, 4, 5]  # new test case to detect the fault
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]  # new test case to detect the fault

