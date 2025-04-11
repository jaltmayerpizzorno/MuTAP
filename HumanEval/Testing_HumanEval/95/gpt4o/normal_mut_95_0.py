def check_dict_case(dict):
    
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():

            if isinstance(key, str) == False:
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                    state = "mixed"
                    break
            else:
                break
        return state == "upper" or state == "lower" 



def test():
        assert check_dict_case({}) == False
    assert check_dict_case({"KEY": 1, "VALUE": 2}) == True
    assert check_dict_case({"key": 1, "value": 2}) == True
    assert check_dict_case({"Key": 1, "Value": 2}) == False
    assert check_dict_case({1: "value", "key": 2}) == False
    assert check_dict_case({"key": 1, "VALUE": 2}) == False
    assert check_dict_case({1: "value", 2: "value"}) == False
    # New test case to detect the change
    assert check_dict_case({"a": "apple", "A": "apple"}) == False
