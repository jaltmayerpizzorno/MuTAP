def greatest_common_divisor(a: int, b: int) -> int:
    
    while b:
        a, b = b, a % b
    return a





def test():

    assert greatest_common_divisor(54, 24) == 6
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(101, 10) == 1
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5
    assert greatest_common_divisor(17, 13) == 1
    assert greatest_common_divisor(100, 25) == 25
    assert greatest_common_divisor(81, 27) == 27
    assert greatest_common_divisor(81, 0) == 81
    assert greatest_common_divisor(54, 24) == 6
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(101, 10) == 1
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5
    assert greatest_common_divisor(17, 13) == 1
    assert greatest_common_divisor(100, 25) == 25
    assert greatest_common_divisor(81, 27) == 27
    assert greatest_common_divisor(81, 0) == 81
    assert greatest_common_divisor(24, 54) == 6  # New test case to detect the fault

    assert greatest_common_divisor(54, 24) == 6
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(101, 10) == 1
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5
    assert greatest_common_divisor(17, 13) == 1
    assert greatest_common_divisor(100, 25) == 25
    assert greatest_common_divisor(81, 27) == 27
    assert greatest_common_divisor(81, 0) == 81
    assert greatest_common_divisor(3, 5) == 1  # New test case to detect the fault

