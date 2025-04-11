def get_odd_collatz(n):
    
    if n%2==0:
        odd_collatz = [] 
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
            
        if n%2 == 1:
            odd_collatz.append(int(n))

    return sorted(odd_collatz)



def test():

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(2) == [1]

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(5) == [1, 5]  # New test case added to detect the potential fault

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(9) == [1, 3, 5, 7, 9, 19, 21, 27]  # New test case to ensure integer division

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(3) == [1, 3, 5, 7]  # New test case to detect fault in code

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(5) == [1, 5]

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(2) == [1]

    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(2) == [1]

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(2) == [1]

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(10) == [1, 5]  # New test case to illustrate the error

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(5) == [1, 5]

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(9) == [1, 3, 5, 7, 9, 11, 17, 23, 25]

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(5) == [1, 5]

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(2) == [1]
    assert get_odd_collatz(3) == [1, 3, 5]
    assert get_odd_collatz(9) == [1, 5, 9, 11, 17, 23, 25, 29]

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(0) == []  # Additional test case to ensure 0 returns an empty list
    assert get_odd_collatz(2) == [1]  # Additional test case to ensure even starting number is handled correctly
    assert get_odd_collatz(15) == [1, 3, 5, 7, 15]  # Additional test case to check for a mix of odd and even numbers in sequence

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(0) == []  # New test case to check for n=0

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(5) == [1, 5]

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(4) == [1]  # New test case to check if even starting value is handled correctly

    assert get_odd_collatz(1) == [1]
    assert get_odd_collatz(6) == [1, 3, 5]
    assert get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(19) == [1, 5, 11, 13, 17, 19, 29]
    assert get_odd_collatz(27) == [1, 5, 23, 27, 31, 35, 41, 47, 53, 61, 71, 91, 103, 107, 121, 137, 155, 161, 167, 175, 233, 251, 263, 283, 319, 325, 377, 395, 425, 433, 445, 479, 577, 593, 719, 911, 1079, 1367, 1619, 2051, 2429, 3077]
    assert get_odd_collatz(0) == []

