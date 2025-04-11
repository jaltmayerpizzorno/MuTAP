def double_the_difference(lst):
    
    return sum([i**2 for i in lst if i > 0 and i%2!=0 and "." not in str(i)])

def test():
def test():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35
    assert double_the_difference([2, 4, 6, 8, 10]) == 0
    assert double_the_difference([-1, -3, -5, -7, -9]) == 0
    assert double_the_difference([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 35
    assert double_the_difference([1.1, 2.2, 3.3, 4.4, 5.5]) == 0
    assert double_the_difference([1, 3, 5, 7, 9]) == 165
#</test>