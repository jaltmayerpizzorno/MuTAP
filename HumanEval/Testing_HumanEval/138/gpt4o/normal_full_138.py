def is_equal_to_sum_even(n):
    
    return n%2 == 0 and n >= 8



def test():

    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(2) == False
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(7) == False
    assert is_equal_to_sum_even(0) == False
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(-8) == False
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(2) == False
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(7) == False
    assert is_equal_to_sum_even(0) == False
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(-8) == False
    assert is_equal_to_sum_even(6) == False  # New test case to detect the potential fault
    assert is_equal_to_sum_even(4) == False  # New test case to detect the potential fault

    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(2) == False
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(7) == False
    assert is_equal_to_sum_even(0) == False
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(-8) == False
    assert is_equal_to_sum_even(4) == False  # New test case
    assert is_equal_to_sum_even(6) == False  # New test case

    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(2) == False
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(7) == False
    assert is_equal_to_sum_even(0) == False
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(-8) == False
    assert is_equal_to_sum_even(6) == False # New test case to detect the change in the code
    assert is_equal_to_sum_even(4) == False # New test case to detect the change in the code

    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(2) == False
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(7) == False
    assert is_equal_to_sum_even(0) == False
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(-8) == False
    assert is_equal_to_sum_even(6) == False   # New test case to detect the fault
    assert is_equal_to_sum_even(4) == False   # New test case to detect the fault

    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(2) == False
    assert is_equal_to_sum_even(10) == True
    assert is_equal_to_sum_even(7) == False
    assert is_equal_to_sum_even(0) == False
    assert is_equal_to_sum_even(12) == True
    assert is_equal_to_sum_even(-8) == False
    assert is_equal_to_sum_even(6) == False  # New test case to detect the fault
    assert is_equal_to_sum_even(4) == False  # New test case to detect the fault

