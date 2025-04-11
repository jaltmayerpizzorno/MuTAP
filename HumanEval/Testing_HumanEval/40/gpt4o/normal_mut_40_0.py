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
    assert triples_sum_to_zero([1, 3, 5, 0]) == False  # New test case
    assert triples_sum_to_zero([1, 3, -2, 1]) == True  # New test case
    assert triples_sum_to_zero([1, 2, 3, 7]) == False  # New test case
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True  # New test case
    assert triples_sum_to_zero([1]) == False  # New test case
