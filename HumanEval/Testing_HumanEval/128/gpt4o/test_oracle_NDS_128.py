def prod_signs(arr):
    
    if not arr: 
        return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])

def test():
    assert prod_signs([1, 2, 3]) == 6
    assert prod_signs([-1, -2, -3]) == -6
    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([1, 0, -3]) == 0
    assert prod_signs([]) == None
    assert prod_signs([-1, 2, -3, 4]) == 10

#</test>