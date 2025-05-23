def prime_fib(n: int):
    
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]





def test():
        assert prime_fib(1) == 2   # The first prime Fibonacci number is 2
    assert prime_fib(2) == 3   # The second prime Fibonacci number is 3
    assert prime_fib(3) == 5   # The third prime Fibonacci number is 5
    assert prime_fib(4) == 13  # The fourth prime Fibonacci number is 13
    assert prime_fib(5) == 89  # The fifth prime Fibonacci number is 89
    assert prime_fib(6) == 233 # The sixth prime Fibonacci number is 233


METADATA = {}

