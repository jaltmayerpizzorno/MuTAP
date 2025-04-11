def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m



def test():
    assert max_element([1, 2, 3, 4, 5]) == 5
    assert max_element([5, 4, 3, 2, 1]) == 5
    assert max_element([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 9
    assert max_element([-1, -2, -3, -4, -5]) == -1
    assert max_element([7]) == 7
    assert max_element([]) == None  # This will raise an error because the function does not handle empty lists
