def generate_integers(a, b):
    
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]


def test():
    assert generate_integers(1, 10) == [2, 4, 6, 8]
    assert generate_integers(3, 7) == [4, 6]
    assert generate_integers(5, 5) == []
    assert generate_integers(9, 12) == []
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(0, 2) == [2]
