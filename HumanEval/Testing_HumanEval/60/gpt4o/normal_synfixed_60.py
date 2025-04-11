def sum_to_n(n: int):
    
    return sum(range(n + 1))



def test():
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(100) == 5050

test()
