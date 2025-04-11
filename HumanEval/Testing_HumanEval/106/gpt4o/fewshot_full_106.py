def f(n):
    
    ret = []
    for i in range(1,n+1):
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret



def test():

    assert f(5) == [1, 2, 6, 24, 15]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(2) == [1, 2]
    assert f(0) == []
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert f(5) == [1, 2, 6, 24, 15]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(2) == [1, 2]
    assert f(0) == []
    assert f(1) == [1]
    assert f(6) == [1, 2, 6, 24, 15, 720]

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert f(5) == [1, 2, 6, 24, 15]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(2) == [1, 2]
    assert f(0) == []
    assert f(6) == [1, 2, 6, 24, 15, 720]  # New test case to check the factorial of an even number beyond 2

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

