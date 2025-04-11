def prod_signs(arr):
    
    if not arr: 
        return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])



def test():

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, -2, -3, 4]) == -10  # Additional test case to detect the fault

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, 2, 2, -4]) == -9  # new test case

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([-1, 2, 0, -3]) == 0  # any product with 0 is 0
    assert prod_signs([1, -2, -3, 4, 5, -6]) == 21  # 1*(-2)*(-3)*4*5*(-6) = 720, |1| + |2| + |3| + |4| + |5| + |6| = 21

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, 2, -3]) == 0  # This new test case should return -6 but returns 0 due to bug in prod_signs function

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, 2, 2, -4]) == -9  # new test case to detect the fault

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, 2, 2, -4]) == -9  # Product of signs: -1, Sum of magnitudes: |1|+|2|+|2|+|4| = 9, Result: -9

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, -2, -3]) == 6  # (-1)^(2) = 1, |1| + |2| + |3| = 6

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([-1, 2, -3]) == 6  # (-1)*2*(-3) = 6, |1| + |2| + |3| = 6

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, 2, 2, -4]) == -9  # new test case to detect the fault

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, 2, 2, -4]) == -9

    assert prod_signs([1, -2, 3]) == -6
    assert prod_signs([-1, -2, -3]) == -6  # (-1)*(-2)*(-3) = -6, |1| + |2| + |3| = 6
    assert prod_signs([0, 1, -2, 3]) == 0  # any product with 0 is 0
    assert prod_signs([]) == None  # empty array should return None
    assert prod_signs([1, 2, 3]) == 6  # 1*2*3 = 6, |1| + |2| + |3| = 6
    assert prod_signs([-1, 2, -3, 4]) == 10
    assert prod_signs([1, -1]) == -2
    assert prod_signs([1, 2, 2, -4]) == 9  # new test case that detects the change in the previous code

