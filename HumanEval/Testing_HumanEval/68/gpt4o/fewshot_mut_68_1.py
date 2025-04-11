def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]



def test():
        assert pluck([4, 2, 0, 3, 0]) == [0, 2]
    assert pluck([1, 2, 3, 4, 2]) == [2, 1]
    assert pluck([2, 2, 2, 2]) == [2, 0]
    assert pluck([3, 3, 3, 3]) == []
    assert pluck([5, 1, 6, 7, 6, 0]) == [0, 5]
#</test>