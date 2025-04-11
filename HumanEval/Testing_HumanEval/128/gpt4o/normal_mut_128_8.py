def prod_signs(arr):
    
    if not arr: 
        return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])



def test():
        assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, -2, -3, 4]) == -10  # Additional test case to detect the fault
