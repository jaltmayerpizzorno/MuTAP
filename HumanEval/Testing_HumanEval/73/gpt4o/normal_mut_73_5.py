def smallest_change(arr):
    
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans



def test():
        assert smallest_change([1, 2, 3, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 2, 1]) == 1
    assert smallest_change([1, 2, 2, 1]) == 0
    assert smallest_change([1, 2, 3, 4, 5]) == 2
    assert smallest_change([]) == 0
    assert smallest_change([1]) == 0
    assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
