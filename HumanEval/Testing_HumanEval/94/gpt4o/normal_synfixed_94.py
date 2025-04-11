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
    assert skjkasdkd([2, 3, 5, 7, 11, 13]) == 4  # 13 is the largest prime, sum of digits is 1+3 = 4
    assert skjkasdkd([15, 21, 24, 30]) == 0    # No primes in the list
    assert skjkasdkd([2, 3, 5, 17, 19]) == 10  # 19 is the largest prime, sum of digits is 1+9 = 10
    assert skjkasdkd([29, 11, 23, 13, 7]) == 11 # 29 is the largest prime, sum of digits is 2+9 = 11
    assert skjkasdkd([]) == 0                 # Empty list should return 0

test()
