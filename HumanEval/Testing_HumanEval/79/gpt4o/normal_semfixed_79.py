def decimal_to_binary(decimal):
    
    return "db" + bin(decimal)[2:] + "db"


def test():
    assert decimal_to_binary(0) == "db0db"
    assert decimal_to_binary(1) == "db1db"
    assert decimal_to_binary(2) == "db10db"
    assert decimal_to_binary(10) == "db1010db"
    assert decimal_to_binary(255) == "db11111111db"
    assert decimal_to_binary(1024) == "db10000000000db"
