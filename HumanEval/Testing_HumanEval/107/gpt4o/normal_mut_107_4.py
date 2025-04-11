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
        # Test case 1: n = 10
    # Palindromes: 1, 2, 3, 4, 5, 6, 7, 8, 9
    # Even palindromes: 2, 4, 6, 8 (4)
    # Odd palindromes: 1, 3, 5, 7, 9 (5)
    assert even_odd_palindrome(10) == (4, 5)

    # Additional test case to catch potential issues:
    # Test case 2: n = 12
    # Palindromes: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11
    # Even palindromes: 2, 4, 6, 8 (4)
    # Odd palindromes: 1, 3, 5, 7, 9, 11 (6)
    assert even_odd_palindrome(12) == (4, 6)
