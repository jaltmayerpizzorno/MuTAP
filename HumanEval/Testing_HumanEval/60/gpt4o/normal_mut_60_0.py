def sum_to_n(n: int):
    
    return sum(range(n + 1))





def test():
        # Original test cases
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(100) == 5050

    # New test cases to detect the fault
    assert sum_to_n(2) == 3
    assert sum_to_n(3) == 6
    assert sum_to_n(4) == 10
    assert sum_to_n(6) == 21
    assert sum_to_n(7) == 28
