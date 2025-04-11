def odd_count(lst):
    
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res


def test():
    assert odd_count(['12345', '24680', '13579']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert odd_count(['12345', '24680', '13579']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert odd_count(['12345', '24680', '13579']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert odd_count(['12345', '24680', '13579']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
