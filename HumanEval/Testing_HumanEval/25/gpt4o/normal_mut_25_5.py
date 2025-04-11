from typing import List


def factorize(n: int) -> List[int]:
    
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact





def test():
        assert factorize(1) == []
    assert factorize(2) == [2]
    assert factorize(3) == [3]
    assert factorize(4) == [2, 2]
    assert factorize(5) == [5]
    assert factorize(6) == [2, 3]
    assert factorize(7) == [7]
    assert factorize(8) == [2, 2, 2]
    assert factorize(9) == [3, 3]
    assert factorize(10) == [2, 5]
    assert factorize(12) == [2, 2, 3]
    assert factorize(15) == [3, 5]
    assert factorize(16) == [2, 2, 2, 2]
    assert factorize(18) == [2, 3, 3]
    assert factorize(20) == [2, 2, 5]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]  # New test case to catch the issue in the docstring
    assert factorize(121) == [11, 11]  # New test case to test prime square number
    assert factorize(49) == [7, 7]  # New test case to test another prime square number

# Running the test case to catch the issue
test()
