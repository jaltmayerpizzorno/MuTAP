def unique_digits(x):
    
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

def test():
    assert unique_digits([135, 246, 357, 789]) == [135, 357, 789]
    assert unique_digits([222, 333, 555, 777]) == [333, 555, 777]
    assert unique_digits([123, 234, 345, 456]) == []
    assert unique_digits([111, 131, 151, 171]) == [111, 131, 151, 171]
    assert unique_digits([246, 864, 975, 333]) == [333]

#</test>