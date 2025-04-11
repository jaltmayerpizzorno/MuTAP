def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]



def test():
        assert pluck([]) == []
    assert pluck([1, 3, 5, 7]) == []
    assert pluck([2, 4, 6, 8]) == [2, 0]
    assert pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    assert pluck([10, 3, 15, 20, 25]) == [10, 0]
    assert pluck([3, 5, 7, 9, 2]) == [2, 4]
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
