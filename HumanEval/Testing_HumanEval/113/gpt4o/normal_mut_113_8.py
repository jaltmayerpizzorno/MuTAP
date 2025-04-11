def odd_count(lst):
    
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res



def test():
        assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3', '11111111']) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(['13579', '24680', '12345']) == ["the number of odd elements 5n the str5ng 5 of the 5nput.", "the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 3n the str3ng 3 of the 3nput."]
    assert odd_count(['', '0000', '1111']) == ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 4n the str4ng 4 of the 4nput."]
