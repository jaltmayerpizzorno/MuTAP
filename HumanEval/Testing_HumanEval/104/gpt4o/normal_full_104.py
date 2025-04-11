def unique_digits(x):
    
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)



def test():

    assert unique_digits([135, 24, 357, 246, 579]) == [135, 357, 579]
    assert unique_digits([22, 44, 66, 11, 33]) == [11, 33]
    assert unique_digits([111, 222, 333, 444, 555]) == [111, 333, 555]
    assert unique_digits([]) == []
    assert unique_digits([1357, 2468, 3579, 4680]) == [1357, 3579]
    assert unique_digits([12, 34, 56, 78, 910]) == []
    assert unique_digits([135, 24, 357, 246, 579]) == [135, 357, 579]
    assert unique_digits([22, 44, 66, 11, 33]) == [11, 33]
    assert unique_digits([111, 222, 333, 444, 555]) == [111, 333, 555]
    assert unique_digits([]) == []
    assert unique_digits([1357, 2468, 3579, 4680]) == [1357, 3579]
    assert unique_digits([12, 34, 56, 78, 910]) == []
    assert unique_digits([135, 246, 357, 579, "135a"]) == [135, 357, 579]  # Testing with a string in the list

    assert unique_digits([135, 24, 357, 246, 579]) == [135, 357, 579]
    assert unique_digits([22, 44, 66, 11, 33]) == [11, 33]
    assert unique_digits([111, 222, 333, 444, 555]) == [111, 333, 555]
    assert unique_digits([]) == []
    assert unique_digits([1357, 2468, 3579, 4680]) == [1357, 3579]
    assert unique_digits([12, 34, 56, 78, 910]) == []
    assert unique_digits([153, 357, 579, 246, 135]) == [135, 153, 357, 579]  # New test case

    assert unique_digits([135, 24, 357, 246, 579]) == [135, 357, 579]
    assert unique_digits([22, 44, 66, 11, 33]) == [11, 33]
    assert unique_digits([111, 222, 333, 444, 555]) == [111, 333, 555]
    assert unique_digits([]) == []
    assert unique_digits([1357, 2468, 3579, 4680]) == [1357, 3579]
    assert unique_digits([12, 34, 56, 78, 910]) == []
    assert unique_digits([13, 57, 91, 24, 80]) == [13, 57, 91]  # new test case to catch the logical error

