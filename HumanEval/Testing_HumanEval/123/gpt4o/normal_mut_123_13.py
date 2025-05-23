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
    assert get_odd_collatz(5) == [1, 5]
