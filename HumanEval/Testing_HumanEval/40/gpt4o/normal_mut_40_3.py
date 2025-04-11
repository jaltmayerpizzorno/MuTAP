def triples_sum_to_zero(l: list):
    
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False





def test():
        assert triples_sum_to_zero([1, -1, 0]) == True
    assert triples_sum_to_zero([1, 2, 3]) == False
    assert triples_sum_to_zero([-1, -2, 3, 0]) == True
    assert triples_sum_to_zero([0, 0, 0]) == True
    assert triples_sum_to_zero([1, 1, -2]) == True
    assert triples_sum_to_zero([5, -5, 10, -10, 0]) == True
    assert triples_sum_to_zero([1, -1, 2, -2, 3, -3]) == True
    assert triples_sum_to_zero([10, 20, 30, 40, 50]) == False
    # New test case to detect the fault
    assert triples_sum_to_zero([1, 2, -3, 4]) == True  # This should return True
    assert triples_sum_to_zero([1, 2, -3, -1, 5, -2]) == True  # This should return True

METADATA = {}
