def x_or_y(n, x, y):
    
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x


def test():
    assert x_or_y(1, 'prime', 'composite') == 'composite'
    assert x_or_y(2, 'prime', 'composite') == 'prime'
    assert x_or_y(3, 'prime', 'composite') == 'prime'
    assert x_or_y(4, 'prime', 'composite') == 'composite'
    assert x_or_y(9, 'prime', 'composite') == 'composite'
    assert x_or_y(13, 'prime', 'composite') == 'prime'
    assert x_or_y(17, 'prime', 'composite') == 'prime'
    assert x_or_y(18, 'prime', 'composite') == 'composite'
    assert x_or_y(19, 'prime', 'composite') == 'prime'
    assert x_or_y(20, 'prime', 'composite') == 'composite'
