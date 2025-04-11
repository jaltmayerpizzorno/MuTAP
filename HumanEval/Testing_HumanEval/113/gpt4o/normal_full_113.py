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
    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3', '11111111']) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(['', '24680', '357']) == ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 3n the str3ng 3 of the 3nput."]
    assert odd_count(['135', '246', '789']) == ["the number of odd elements 3n the str3ng 3 of the 3nput.", "the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 2n the str2ng 2 of the 2nput."]

    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3', '11111111']) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(['24680']) == ["the number of odd elements 0n the str0ng 0 of the 0nput."]
    assert odd_count(['13579', '02468']) == ["the number of odd elements 5n the str5ng 5 of the 5nput.", "the number of odd elements 0n the str0ng 0 of the 0nput."]

    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3', "11111111"]) == ["the number of odd elements 1n the str1ng 1 of the 1nput.",
    assert odd_count(['246']) == ["the number of odd elements 0n the str0ng 0 of the 0nput."]
    assert odd_count(['97531']) == ["the number of odd elements 5n the str5ng 5 of the 5nput."]
    assert odd_count(['0', '0']) == ["the number of odd elements 0n the str0ng 0 of the 0nput.",

    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3', '11111111']) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(['12345', '24680', '13579']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert odd_count(['']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.']
    assert odd_count(['2222', '3333', '4444']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 4n the str4ng 4 of the 4nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.']

    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3', '11111111']) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(['24680']) == ["the number of odd elements 0n the str0ng 0 of the 0nput."]
    assert odd_count(['13579']) == ["the number of odd elements 5n the str5ng 5 of the 5nput."]
    assert odd_count(['']) == ["the number of odd elements 0n the str0ng 0 of the 0nput."]

    assert odd_count(['12345', '24680', '13579']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert odd_count(['3', '11111111']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.', 'the number of odd elements 8n the str8ng 8 of the 8nput.']
    assert odd_count(['']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.']
    assert odd_count(['2', '4', '6']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.']
    assert odd_count(['13579', '24680', '1234567890']) == ['the number of odd elements 5n the str5ng 5 of the 5nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']

    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3', '11111111']) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(['24680', '97531']) == ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 5n the str5ng 5 of the 5nput."]
    assert odd_count(['111222333', '444555666']) == ["the number of odd elements 6n the str6ng 6 of the 6nput.", "the number of odd elements 3n the str3ng 3 of the 3nput."]

    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3', '11111111']) == ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
    assert odd_count(['13579', '24680', '12345']) == ["the number of odd elements 5n the str5ng 5 of the 5nput.", "the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 3n the str3ng 3 of the 3nput."]
    assert odd_count(['', '0000', '1111']) == ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 4n the str4ng 4 of the 4nput."]

    assert odd_count(['1234567']) == ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    assert odd_count(['3', '11111111']) == ["the number of odd elements 1n the str1ng 1 of the 1nput.",
    assert odd_count(['']) == ["the number of odd elements 0n the str0ng 0 of the 0nput."]
    assert odd_count(['24680', '12345', '']) == ["the number of odd elements 0n the str0ng 0 of the 0nput.",

    assert odd_count(['12345', '24680', '13579']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 5n the str5ng 5 of the 5nput.']
    assert odd_count(['111', '222', '333', '444', '555']) == ['the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.', 'the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 3n the str3ng 3 of the 3nput.']
    assert odd_count(['0000', '1234', '5678']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.', 'the number of odd elements 2n the str2ng 2 of the 2nput.']
    assert odd_count(['9']) == ['the number of odd elements 1n the str1ng 1 of the 1nput.']
    assert odd_count(['']) == ['the number of odd elements 0n the str0ng 0 of the 0nput.']

