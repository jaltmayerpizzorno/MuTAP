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
    assert get_odd_collatz(7) == [1, 3, 5, 7, 11]
    assert get_odd_collatz(19) == [1, 3, 5, 7, 9, 11, 15, 17, 19, 27, 29, 31, 35, 45, 55]
    assert get_odd_collatz(27) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 85, 87, 89, 91, 93, 95, 97, 99, 101]
