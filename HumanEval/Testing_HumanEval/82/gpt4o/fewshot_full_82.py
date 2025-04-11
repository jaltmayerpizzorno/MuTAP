def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True



def test():

    assert prime_length("hello") == True
    assert prime_length("abcd") == False
    assert prime_length("a") == False
    assert prime_length("abc") == True
    assert prime_length("") == False
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert prime_length("hello") == True
    assert prime_length("abcdcba") == True
    assert prime_length("kittens") == True
    assert prime_length("orange") == False

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert prime_length("hello world") == False  # Length is 11, which is prime
    assert prime_length("abcdefghij") == False  # Length is 10, which is not prime

    assert prime_length("hello") == True
    assert prime_length("abcd") == False
    assert prime_length("a") == False
    assert prime_length("abc") == True
    assert prime_length("") == False
    assert prime_length("abcdcb") == False  # Additional test case

    assert prime_length("hello") == True
    assert prime_length("abcd") == False
    assert prime_length("a") == False
    assert prime_length("abc") == True
    assert prime_length("") == False
    assert prime_length("abcdcba") == True
    assert prime_length("kittens") == True
    assert prime_length("orange") == False

    assert prime_length("hello") == True
    assert prime_length("abcd") == False
    assert prime_length("a") == False
    assert prime_length("abc") == True
    assert prime_length("") == False
    assert prime_length("ab") == True  # New test case: length is 2 which is prime
    assert prime_length("abcf") == True  # New test case: length is 4 which is not prime
    assert prime_length("abcdefghij") == False  # New test case: length is 10 which is not prime
    assert prime_length("abcdefgh") == True  # New test case: length is 8 which is not prime

