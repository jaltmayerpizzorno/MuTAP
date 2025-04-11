def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

def test():
    assert add([1, 2, 3, 4, 5, 6]) == 2
    assert add([0, 2, 4, 6, 8, 10]) == 16
    assert add([1, 3, 5, 7, 9, 11]) == 0
    assert add([2, 4, 6, 8, 10, 12, 14]) == 12
    assert add([]) == 0
    assert add([1]) == 0
