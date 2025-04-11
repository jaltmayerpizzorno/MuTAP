def special_factorial(n):
    
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact



def test():
        assert special_factorial(0) == 1  # 0! is 1, so special factorial is also 1
    assert special_factorial(1) == 1  # 1! is 1, so special factorial is 1
    assert special_factorial(2) == 2  # 2! = 2, so special factorial is 1 * 2 = 2
    assert special_factorial(3) == 12  # 3! = 6, so special factorial is 1 * 2 * 6 = 12
    assert special_factorial(4) == 288  # 4! = 24, so special factorial is 1 * 2 * 6 * 24 = 288
    assert special_factorial(5) == 34560  # 5! = 120, so special factorial is 1 * 2 * 6 * 24 * 120 = 34560
    assert special_factorial(6) == 24883200  # 6! = 720, so special factorial is 1 * 2 * 6 * 24 * 120 * 720 = 24883200
    assert special_factorial(7) == 125411328000  # 7! = 5040, so special factorial is 1 * 2 * 6 * 24 * 120 * 720 * 5040 = 125411328000
    assert special_factorial(8) == 645241282560000  # 8! = 40320, so special factorial is 1 * 2 * 6 * 24 * 120 * 720 * 5040 * 40320 = 645241282560000
    assert special_factorial(9) == 3315318162720000000  # 9! = 362880, so special factorial is 1 * 2 * 6 * 24 * 120 * 720 * 5040 * 40320 * 362880 = 3315318162720000000
    assert special_factorial(10) == 171001225272419942400000  # 10! = 3628800, so special factorial is 1 * 2 * 6 * 24 * 120 * 720 * 5040 * 40320 * 362880 * 3628800 = 171001225272419942400000
