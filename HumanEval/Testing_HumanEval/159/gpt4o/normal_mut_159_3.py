def eat(number, need, remaining):
    
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]



def test():
        assert eat(5, 3, 10) == [8, 7]
    assert eat(5, 10, 3) == [8, 0]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(10, 5, 5) == [15, 0]
    assert eat(2, 1, 1) == [3, 0]
    assert eat(4, 8, 9) == [12, 1]  # New test case to detect the change
