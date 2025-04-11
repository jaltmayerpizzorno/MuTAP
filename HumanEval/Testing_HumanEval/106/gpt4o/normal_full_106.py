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

    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(6) == [1, 2, 6, 24, 15, 720]
    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(6) == [1, 2, 6, 24, 15, 720]
    assert f(0) == []  # test case to check the function with 0 input
    assert f(-1) == []  # test case to check the function with negative input

    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(6) == [1, 2, 6, 24, 15, 720]
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]

    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(6) == [1, 2, 6, 24, 15, 720]
    assert f(10) == [1, 2, 6, 24, 15, 720, 28, 40320, 45, 3628800]  # New test case to catch the issue

    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(6) == [1, 2, 6, 24, 15, 720]
    assert f(2) == [1, 2]  # Not expecting [1, 1] if the fault is present

    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(6) == [1, 2, 6, 24, 15, 720]
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]

    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(6) == [1, 2, 6, 24, 15, 720]
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]  # New test case to detect the fault

    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(6) == [1, 2, 6, 24, 15, 720]
    assert f(0) == []
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]
    assert f(8) == [1, 2, 6, 24, 15, 720, 28, 40320]
    assert f(10) == [1, 2, 6, 24, 15, 720, 28, 40320, 45, 3628800]

    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [1, 2, 6]
    assert f(4) == [1, 2, 6, 24]
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(6) == [1, 2, 6, 24, 15, 720]
    assert f(0) == []
    assert f(10) == [1, 2, 6, 24, 15, 720, 28, 40320, 45, 3628800]
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]

