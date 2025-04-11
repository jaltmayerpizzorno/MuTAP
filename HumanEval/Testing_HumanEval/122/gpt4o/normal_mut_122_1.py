def add_elements(arr, k):
    
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)



def test():
        assert add_elements([1, 23, 456, 78], 2) == 24
    assert add_elements([1, 23, 456, 78], 3) == 24
    assert add_elements([10, 20, 30, 40], 4) == 100
    assert add_elements([100, 200, 300], 3) == 0
    assert add_elements([1, 2, 3, 4], 0) == 0
    assert add_elements([], 2) == 0
    # New test case to detect the change
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24  # sum of 21 + 3
