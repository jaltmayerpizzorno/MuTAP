def hex_key(num):
    
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total



def test():
        assert hex_key("123") == 2
    assert hex_key("ABC") == 1
    assert hex_key("753") == 3
    assert hex_key("2468") == 1
    assert hex_key("BDF") == 2
    # New test cases to detect the change
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2
