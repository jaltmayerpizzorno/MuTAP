def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]


def test():
    assert pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    assert pluck([1, 3, 5, 7, 9]) == []
    assert pluck([4, 3, 2, 1]) == [2, 2]
    assert pluck([]) == []
    assert pluck([10, 15, 20, 25, 30]) == [10, 0]
