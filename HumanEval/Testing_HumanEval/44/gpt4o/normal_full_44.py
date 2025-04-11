def change_base(x: int, base: int):
    
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret







def test():

    assert change_base(10, 2) == "1010"
    assert change_base(255, 16) == 1515
    assert change_base(0, 8) == 
    assert change_base(100, 10) == "100"
    assert change_base(7, 3) == "21"
    assert change_base(1, 2) == "1"
    assert change_base(64, 8) == "100"
