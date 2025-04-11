def common(l1: list, l2: list):
    
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))




def test():
    assert common([1, 2, 3], [3, 4, 5]) == [3]
    assert common([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3]
    assert common([], [1, 2, 3]) == []
    assert common([1, 2, 3], []) == []
    assert common([1, 2, 3], [4, 5, 6]) == []
    assert common([1, 'a', 3], ['a', 'b', 3]) == [3, 'a']    assert common(['apple', 'banana'], ['banana', 'cherry']) == ['banana']
