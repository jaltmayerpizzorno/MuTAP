def prime_length(string):
    
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True



def test():

    assert prime_length("") == False
    assert prime_length("a") == False
    assert prime_length("ab") == True
    assert prime_length("abc") == True
    assert prime_length("abcd") == False
    assert prime_length("abcde") == True
    assert prime_length("abcdef") == False
    assert prime_length("abcdefg") == True
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghi") == False
    assert prime_length("abcdefghij") == False
    assert prime_length("abcdefghijk") == True
    assert prime_length("Hello") == False
    assert prime_length("abcdcba") == False
    assert prime_length("kittens") == False
    assert prime_length("orange") == False
    assert prime_length("") == False
    assert prime_length("a") == False
    assert prime_length("ab") == True
    assert prime_length("abc") == True
    assert prime_length("abcd") == False
    assert prime_length("abcde") == True
    assert prime_length("abcdef") == False
    assert prime_length("abcdefg") == True
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghi") == False
    assert prime_length("abcdefghij") == False
    assert prime_length("abcdefghijk") == True

    assert prime_length("") == False
    assert prime_length("a") == False
    assert prime_length("ab") == True
    assert prime_length("abc") == True
    assert prime_length("abcd") == False
    assert prime_length("abcde") == True
    assert prime_length("abcdef") == False
    assert prime_length("abcdefg") == True
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghi") == False
    assert prime_length("abcdefghij") == False
    assert prime_length("abcdefghijk") == True
    assert prime_length("abcccc") == True
    assert prime_length("Hello") == True
    assert prime_length("abcdcba") == True
    assert prime_length("kittens") == True
    assert prime_length("orange") == False

    assert prime_length("") == False
    assert prime_length("a") == False
    assert prime_length("ab") == True
    assert prime_length("abc") == True
    assert prime_length("abcd") == False
    assert prime_length("abcde") == True
    assert prime_length("abcdef") == False
    assert prime_length("abcdefg") == True
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghi") == False
    assert prime_length("abcdefghij") == False
    assert prime_length("abcdefghijk") == True
    assert prime_length("Hello") == False
    assert prime_length("abcdcba") == True
    assert prime_length("kittens") == True
    assert prime_length("orange") == True

    assert prime_length("") == False
    assert prime_length("a") == False
    assert prime_length("ab") == True
    assert prime_length("abc") == True
    assert prime_length("abcd") == False
    assert prime_length("abcde") == True
    assert prime_length("abcdef") == False
    assert prime_length("abcdefg") == True
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghi") == False
    assert prime_length("abcdefghij") == False
    assert prime_length("abcdefghijk") == True
    assert prime_length("abcdefghijklm") == True  # 13 is a prime number

    assert prime_length("") == False
    assert prime_length("a") == False
    assert prime_length("ab") == True
    assert prime_length("abc") == True
    assert prime_length("abcd") == False
    assert prime_length("abcde") == True
    assert prime_length("abcdef") == False
    assert prime_length("abcdefg") == True
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghi") == False
    assert prime_length("abcdefghij") == False
    assert prime_length("abcdefghijk") == True
    assert prime_length("abcdefghijklm") == False  # New test case

    assert prime_length("") == False
    assert prime_length("a") == False
    assert prime_length("ab") == False  # This should return True
    assert prime_length("abc") == False  # This should return True
    assert prime_length("abcd") == True  # This should return False
    assert prime_length("abcde") == True
    assert prime_length("abcdef") == False
    assert prime_length("abcdefg") == True
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghi") == False
    assert prime_length("abcdefghij") == False
    assert prime_length("abcdefghijk") == True

    assert prime_length("") == False
    assert prime_length("a") == False
    assert prime_length("ab") == True
    assert prime_length("abc") == True
    assert prime_length("abcd") == False
    assert prime_length("abcde") == True
    assert prime_length("abcdef") == False
    assert prime_length("abcdefg") == True
    assert prime_length("abcdefgh") == False
    assert prime_length("abcdefghi") == False
    assert prime_length("abcdefghij") == False
    assert prime_length("abcdefghijk") == True
    assert prime_length("ab") == True  # Length 2 is prime

