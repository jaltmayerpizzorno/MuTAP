def flip_case(string: str) -> str:
    
    return string.swapcase()





def test():

    assert flip_case("Hello") == "hELLO"
    assert flip_case("WORLD") == "world"
    assert flip_case("123AbC") == "123aBc"
    assert flip_case("!@#") == "!@#"
    assert flip_case("") == ""
    assert flip_case("Python3.8") == "pYTHON3.8"
