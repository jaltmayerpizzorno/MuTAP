def skjkasdkd(lst):
    
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result




def test():
        assert skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10  # 181 is the largest prime, sum of digits is 1+8+1 = 10
    assert skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25  # 4597 is the largest prime, sum of digits is 4+5+9+7 = 25
    assert skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]) == 13  # 5107 is the largest prime, sum of digits is 5+1+0+7 = 13
    assert skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]) == 11  # 83 is the largest prime, sum of digits is 8+3 = 11
    assert skjkasdkd([0, 81, 12, 3, 1, 21]) == 3  # 3 is the largest prime, sum of digits is 3
    assert skjkasdkd([2, 3, 5, 7, 11, 13]) == 4  # 13 is the largest prime, sum of digits is 1+3 = 4
    assert skjkasdkd([15, 21, 24, 30]) == 0  # No primes in the list
    assert skjkasdkd([2, 3, 5, 17, 19]) == 10  # 19 is the largest prime, sum of digits is 1+9 = 10
    assert skjkasdkd([29, 11, 23, 13, 7]) == 11  # 29 is the largest prime, sum of digits is 2+9 = 11
    assert skjkasdkd([]) == 0  # Empty list should return 0
