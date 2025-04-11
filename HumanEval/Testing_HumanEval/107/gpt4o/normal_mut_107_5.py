def even_odd_palindrome(n):
    
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n+1):
        if i%2 == 1 and is_palindrome(i):
                odd_palindrome_count += 1
        elif i%2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)



def test():
    def test():
    # Test case 1: n = 10
    # Palindromes: 1, 2, 3, 4, 5, 6, 7, 8, 9
    # Even palindromes: 2, 4, 6, 8 (4)
    # Odd palindromes: 1, 3, 5, 7, 9 (5)
    assert even_odd_palindrome(10) == (4, 5)

    # Additional test case 2: n = 12
    # Palindromes: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11
    # Even palindromes: 2, 4, 6, 8 (4)
    # Odd palindromes: 1, 3, 5, 7, 9, 11 (6)
    assert even_odd_palindrome(12) == (4, 6)

    # Additional test case 3: n = 20
    # Palindromes: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11
    # Even palindromes: 2, 4, 6, 8 (4)
    # Odd palindromes: 1, 3, 5, 7, 9, 11 (6)
    assert even_odd_palindrome(20) == (4, 6)

    # Additional test case 4: n = 1
    # Palindromes: 1
    # Even palindromes: 0
    # Odd palindromes: 1 (1)
    assert even_odd_palindrome(1) == (0, 1)

    # Additional test case 5: n = 100
    # Palindromes: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99
    # Even palindromes: 2, 4, 6, 8, 22, 44, 66, 88 (8)
    # Odd palindromes: 1, 3, 5, 7, 9, 11, 33, 55, 77, 99 (10)
    assert even_odd_palindrome(100) == (8, 10)
