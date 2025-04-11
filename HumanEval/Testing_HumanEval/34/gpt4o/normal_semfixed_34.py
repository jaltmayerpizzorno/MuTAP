def unique(l: list):
    
    return sorted(list(set(l)))




def test():
    assert unique([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique([]) == []
    assert unique([5, 5, 5, 5, 5]) == [5]
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique([3, 1, 2, 3, 4]) == [1, 2, 3, 4]
    assert unique([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert unique(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']
    assert unique(['apple', 'banana', 'apple']) == ['apple', 'banana']
    assert unique([1.1, 2.2, 1.1, 3.3, 2.2]) == [1.1, 2.2, 3.3]
    assert unique([True, False, True, False]) == [False, True]
