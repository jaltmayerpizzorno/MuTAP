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
        assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>

#<code>

from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
#</code>

#<test>

def test():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>

#<code>

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
#</code>

#<test>

def test():
    assert is_multiply_prime(30) == True  # 2*3*5
    assert is_multiply_prime(60) == False # 2*2*3*5, not a product of three distinct primes
    assert is_multiply_prime(105) == True # 3*5*7
    assert is_multiply_prime(231) == True # 3*7*11
    assert is_multiply_prime(50) == True

#</test>

#<test>

def test():
    assert is_multiply_prime(2) == False  # 2 is a prime number, not a product of three distinct primes
    assert is_multiply_prime(9) == False  # 9 is 3*3, not a product of three distinct primes
    assert is_multiply_prime(105) == True # 3*5*7

#</test>
