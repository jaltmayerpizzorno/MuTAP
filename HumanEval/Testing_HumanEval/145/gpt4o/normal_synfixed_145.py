def order_by_points(nums):
    
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)

def test():
    assert order_by_points([56, -33, 12, -45, 23]) == [-33, 12, 23, -45, 56]
    assert order_by_points([0, 19, -28, 37, -46]) == [0, 19, -28, 37, -46]
    assert order_by_points([5, -1, 3, -7, 8]) == [-1, 3, 5, -7, 8]
    assert order_by_points([10, -20, 30, -40, 50]) == [10, -20, 30, -40, 50]
    assert order_by_points([-99, 88, 77, -66, 55]) == [55, -66, 77, 88, -99]

test()
