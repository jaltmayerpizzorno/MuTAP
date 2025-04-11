def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

def test():
    assert maximum([1, 3, 2, 7, 5, 6], 3) == [5, 6, 7]
    assert maximum([1, 2, 3, 4, 5], 0) == []
    assert maximum([5, 4, 3, 2, 1], 2) == [4, 5]
    assert maximum([9, 8, 7, 10, 6], 1) == [10]
    assert maximum([-1, -2, -3, -4, -5], 2) == [-1, -2]
    assert maximum([100, 200, 300], 3) == [100, 200, 300]
