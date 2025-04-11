def is_sorted(lst):
    
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
    



def test():
        assert is_sorted([1, 2, 2, 3]) == True
    assert is_sorted([1, 2, 2, 2, 3]) == False
    assert is_sorted([1, 3, 2, 4]) == False
    assert is_sorted([]) == True
    assert is_sorted([1]) == True
    assert is_sorted([2, 1]) == False
    assert is_sorted([1, 1, 2, 2]) == True
    assert is_sorted([1, 1, 1, 2]) == False
    assert is_sorted([1, 3, 3, 5, 5]) == True
    assert is_sorted([1, 5, 5, 3]) == False
    assert is_sorted([2, 2, 2, 2]) == False  # New test case to detect the fault
