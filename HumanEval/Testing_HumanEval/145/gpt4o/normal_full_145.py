def order_by_points(nums):
    
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)



def test():

    assert order_by_points([56, -33, 12, -45, 23]) == [-33, -45, 12, 23, 56]
    assert order_by_points([0, 19, -28, 37, -46]) == [0, -46, -28, 19, 37]
    assert order_by_points([5, -1, 3, -7, 8]) == [-7, -1, 3, 5, 8]
    assert order_by_points([10, -20, 30, -40, 50]) == [-40, -20, 10, 30, 50]
    assert order_by_points([-99, 88, 77, -66, 55]) == [-99, -66, 55, 77, 88]
    assert order_by_points([56, -33, 12, -45, 23]) == [-33, -45, 12, 23, 56]
    assert order_by_points([0, 19, -28, 37, -46]) == [0, -46, -28, 19, 37]
    assert order_by_points([5, -1, 3, -7, 8]) == [-7, -1, 3, 5, 8]
    assert order_by_points([10, -20, 30, -40, 50]) == [-40, -20, 10, 30, 50]
    assert order_by_points([-99, 88, 77, -66, 55]) == [-99, -66, 55, 77, 88]
    assert order_by_points([100, -100, 0, -1, 1]) == [0, -1, 1, -100, 100]

    assert order_by_points([56, -33, 12, -45, 23]) == [-33, -45, 12, 23, 56]
    assert order_by_points([0, 19, -28, 37, -46]) == [0, -46, -28, 19, 37]
    assert order_by_points([5, -1, 3, -7, 8]) == [-7, -1, 3, 5, 8]
    assert order_by_points([10, -20, 30, -40, 50]) == [-40, -20, 10, 30, 50]
    assert order_by_points([-99, 88, 77, -66, 55]) == [-99, -66, 55, 77, 88]
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, -12, 1, 11]  # New test case

    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []

    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []

    assert order_by_points([56, -33, 12, -45, 23]) == [-33, -45, 12, 23, 56]
    assert order_by_points([0, 19, -28, 37, -46]) == [0, -46, -28, 19, 37]
    assert order_by_points([5, -1, 3, -7, 8]) == [-7, -1, 3, 5, 8]
    assert order_by_points([10, -20, 30, -40, 50]) == [-40, -20, 10, 30, 50]
    assert order_by_points([-99, 88, 77, -66, 55]) == [-99, -66, 55, 77, 88]
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([56, -33, 12, -45, 23]) == [-33, -45, 12, 23, 56]
    assert order_by_points([0, 19, -28, 37, -46]) == [0, -46, -28, 19, 37]
    assert order_by_points([5, -1, 3, -7, 8]) == [-7, -1, 3, 5, 8]
    assert order_by_points([10, -20, 30, -40, 50]) == [-40, -20, 10, 30, 50]
    assert order_by_points([-99, 88, 77, -66, 55]) == [-99, -66, 55, 77, 88]

    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, -12, 1, 11]
    assert order_by_points([]) == []
    assert order_by_points([56, -33, 12, -45, 23]) == [-33, -45, 12, 23, 56]
    assert order_by_points([0, 19, -28, 37, -46]) == [0, -46, -28, 19, 37]
    assert order_by_points([5, -1, 3, -7, 8]) == [-7, -1, 3, 5, 8]
    assert order_by_points([10, -20, 30, -40, 50]) == [-40, -20, 10, 30, 50]
    assert order_by_points([-99, 88, 77, -66, 55]) == [-99, -66, 55, 77, 88]

    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []

    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []

    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([15, -24, 36, -47, 58]) == [-47, -24, 15, 36, 58]

    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([56, -33, 12, -45, 23]) == [-33, -45, 12, 23, 56]
    assert order_by_points([0, 19, -28, 37, -46]) == [0, -46, -28, 19, 37]
    assert order_by_points([5, -1, 3, -7, 8]) == [-7, -1, 3, 5, 8]
    assert order_by_points([10, -20, 30, -40, 50]) == [-40, -20, 10, 30, 50]
    assert order_by_points([-99, 88, 77, -66, 55]) == [-99, -66, 55, 77, 88]
    assert order_by_points([123, -321, 213, -132, 312]) == [-132, -321, 123, 213, 312]

    assert order_by_points([12, 21, -3, 30, -12]) == [-3, 12, 21, -12, 30]
    assert order_by_points([100, 91, -19, -28, 37]) == [100, 91, 37, -19, -28]
    assert order_by_points([405, -504, 123, -312, 213]) == [-504, 123, -312, 213, 405]
    assert order_by_points([45, -54, 99, -99, 27]) == [45, -54, 27, 99, -99]
    assert order_by_points([]) == []

    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([20, 2, -2, 22]) == [-2, 2, 20, 22]
    assert order_by_points([0, 19, -28, 37, -46]) == [0, -46, -28, 19, 37]
    assert order_by_points([5, -1, 3, -7, 8]) == [-7, -1, 3, 5, 8]
    assert order_by_points([10, -20, 30, -40, 50]) == [-40, -20, 10, 30, 50]
    assert order_by_points([-99, 88, 77, -66, 55]) == [-99, -66, 55, 77, 88]

