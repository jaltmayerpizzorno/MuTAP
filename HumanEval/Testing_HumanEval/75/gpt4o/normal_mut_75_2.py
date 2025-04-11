def is_multiply_prime(a):
    
    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True




    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False



def test():
        assert is_multiply_prime(30) == True, "Test case 1 failed"  # 2 * 3 * 5
    assert is_multiply_prime(60) == False, "Test case 2 failed"
    assert is_multiply_prime(8) == True, "Test case 3 failed"  # 2 * 2 * 2
    assert is_multiply_prime(105) == True, "Test case 4 failed" # 3 * 5 * 7
    assert is_multiply_prime(1) == False, "Test case 5 failed" # 1 is not a product of primes
    assert is_multiply_prime(1001) == True, "Test case 6 failed" # 7 * 11 * 13
    assert is_multiply_prime(97) == False, "Test case 7 failed" # 97 is a prime number itself, not a product of 3 primes

test()
