def odd_count(lst):
    
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res

def test():
    assert odd_count(['12345', '24680', '13579']) == [
        'the number of odd elements 3 in the string 12345',
        'the number of odd elements 0 in the string 24680',
        'the number of odd elements 5 in the string 13579'
    ]
    assert odd_count(['11111', '22222', '33333']) == [
        'the number of odd elements 5 in the string 11111',
        'the number of odd elements 0 in the string 22222',
        'the number of odd elements 5 in the string 33333'
    ]
    assert odd_count(['', '123', '456']) == [
        'the number of odd elements 0 in the string ',
        'the number of odd elements 2 in the string 123',
        'the number of odd elements 0 in the string 456'
    ]
    assert odd_count(['00000', '99999', '1234567890']) == [
        'the number of odd elements 0 in the string 00000',
        'the number of odd elements 5 in the string 99999',
        'the number of odd elements 5 in the string 1234567890'
    ]
    print("All test cases pass")

test()
