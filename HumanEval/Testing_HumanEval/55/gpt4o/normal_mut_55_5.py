def fib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)





def test():
        assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(10) == 55
    assert fib(15) == 610  # Additional test case to catch the fault
    assert fib(20) == 6765  # Another additional test case for larger input
