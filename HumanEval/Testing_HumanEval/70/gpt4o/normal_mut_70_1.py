def strange_sort_list(lst):
    
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res



def test():
        assert strange_sort_list([4, 3, 2, 1]) == [1, 4, 2, 3]
    assert strange_sort_list([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert strange_sort_list([5, 2, 9, 3, 8]) == [2, 9, 3, 8, 5]
    assert strange_sort_list([3]) == [3]
    assert strange_sort_list([]) == []
    assert strange_sort_list([7, 3, 5, 3, 2]) == [2, 7, 3, 5, 3]
