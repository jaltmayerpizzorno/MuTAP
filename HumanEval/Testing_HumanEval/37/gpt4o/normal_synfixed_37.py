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
    assert sort_even([4, 1, 2, 3]) == [2, 1, 4, 3]
    assert sort_even([10, 9, 8, 7, 6, 5]) == [6, 9, 8, 7, 10, 5]
    assert sort_even([3, 1]) == [3, 1]
    assert sort_even([1]) == [1]
    assert sort_even([]) == []
    assert sort_even([5, 8, 6, 7, 3, 2, 1, 4]) == [1, 8, 3, 7, 5, 2, 6, 4]

test()
