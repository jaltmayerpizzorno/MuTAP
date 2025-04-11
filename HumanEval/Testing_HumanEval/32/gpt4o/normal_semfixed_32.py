import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    begin, end = -1., 1.
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin




def test():
    assert math.isclose(find_zero([1, -3, 2]), 1.0, rel_tol=1e-9)  # x^2 - 3x + 2 = 0 has roots at x=1 and x=2    assert math.isclose(find_zero([1, 0, -4]), 2.0, rel_tol=1e-9)  # x^2 - 4 = 0 has roots at x=2 and x=-2    assert math.isclose(find_zero([1, 0, 0, -1]), 1.0, rel_tol=1e-9)  # x^3 - 1 = 0 has a root at x=1
    assert math.isclose(find_zero([0, 1]), 0.0, rel_tol=1e-9)  # x = 0