def unique_digits(x):
    
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)



def test():
        assert unique_digits([152, 323, 1422, 10]) == []
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
    assert unique_digits([242, 333, 555, 777]) == [333, 555, 777]
    assert unique_digits([82, 131, 151, 171]) == [131, 151, 171]
    assert unique_digits([246, 864, 975, 333]) == [333, 975]
#</test>