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
    assert eat(5, 3, 10) == [8, 7]
    assert eat(5, 10, 3) == [8, 0]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(10, 5, 5) == [15, 0]
    assert eat(2, 1, 1) == [3, 0]
    assert eat(4, 8, 9) == [12, 1]  # New test case to detect the change

    assert eat(5, 3, 10) == [8, 7]
    assert eat(5, 10, 3) == [8, 0]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(10, 5, 5) == [15, 0]
    assert eat(2, 1, 1) == [3, 0]
    assert eat(4, 8, 9) == [12, 1]

    assert eat(5, 3, 10) == [8, 7]
    assert eat(5, 10, 3) == [8, 0]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(10, 5, 5) == [15, 0]
    assert eat(2, 1, 1) == [3, 0]
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

    assert eat(5, 3, 10) == [8, 7]
    assert eat(5, 10, 3) == [8, 0]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(10, 5, 5) == [15, 0]
    assert eat(2, 1, 1) == [3, 0]
    assert eat(10, 5, 3) == [13, 0]  # new test case to detect fault

    assert eat(5, 3, 10) == [8, 7]
    assert eat(5, 10, 3) == [8, 0]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(10, 5, 5) == [15, 0]
    assert eat(2, 1, 1) == [3, 0]
    assert eat(5, 6, 10) == [11, 4]  # New test case to detect the change

    assert eat(5, 3, 10) == [8, 7]
    assert eat(5, 10, 3) == [8, 0]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(10, 5, 5) == [15, 0]
    assert eat(2, 1, 1) == [3, 0]
    assert eat(4, 8, 9) == [12, 1]  # New test case
    assert eat(5, 5, 10) == [10, 5]  # New test case

