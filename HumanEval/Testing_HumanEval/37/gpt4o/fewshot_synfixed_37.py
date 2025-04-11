def sort_even(l: list):
    
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans



def test():
    assert sort_even([5, 2, 4, 3, 7, 1]) == [4, 2, 5, 3, 7, 1]
    assert sort_even([10, 5, 8, 2, 6]) == [6, 5, 8, 2, 10]
    assert sort_even([1, 3, 2, 7, 4]) == [1, 3, 2, 7, 4]
    assert sort_even([9, 8, 7, 6, 5, 4]) == [5, 8, 7, 6, 9, 4]
    assert sort_even([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
#</test>