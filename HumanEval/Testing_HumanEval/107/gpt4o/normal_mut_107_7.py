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
        # Test case 2: n = 20
    # Palindromes: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11
    # Even palindromes: 2, 4, 6, 8 (4)
    # Odd palindromes: 1, 3, 5, 7, 9, 11 (6)
    assert even_odd_palindrome(20) == (4, 6)

    # The above test case should fail if the incorrect code snippet is used:
    # elif (i % 2 == 0 or is_palindrome(i)):

    # Additional test case to ensure correctness
    # Test case 3: n = 50
    # Palindromes: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22
    # Even palindromes: 2, 4, 6, 8, 22 (5)
    # Odd palindromes: 1, 3, 5, 7, 9, 11 (6)
    assert even_odd_palindrome(50) == (5, 6)
