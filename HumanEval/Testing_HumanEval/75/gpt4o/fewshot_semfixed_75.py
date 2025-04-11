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
    assert is_multiply_prime(30) == True  # 2*3*5
    assert is_multiply_prime(60) == False # 2*2*3*5, not a product of three distinct primes
    assert is_multiply_prime(105) == True # 3*5*7
    assert is_multiply_prime(231) == True # 3*7*11
    assert is_multiply_prime(50) == True
