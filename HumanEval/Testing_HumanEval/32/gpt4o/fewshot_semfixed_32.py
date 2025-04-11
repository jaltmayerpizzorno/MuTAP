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
    assert math.isclose(find_zero([1, 0, -1]), 0.0, abs_tol=1e-10)    assert math.isclose(find_zero([1, 0, 0, -1]), 1.0, abs_tol=1e-10)
    assert math.isclose(find_zero([1, -3, 2]), 1.0, abs_tol=1e-10)    assert math.isclose(find_zero([2, -3, 1]), 0.5, abs_tol=1e-10)    assert math.isclose(find_zero([1, 0, 0, 0, -1]), 1.0, abs_tol=1e-10)