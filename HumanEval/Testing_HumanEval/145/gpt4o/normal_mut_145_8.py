def order_by_points(nums):
    
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)



def test():
        assert order_by_points([12, 21, -3, 30, -12]) == [-3, 12, 21, -12, 30]
    assert order_by_points([100, 91, -19, -28, 37]) == [100, 91, 37, -19, -28]
    assert order_by_points([405, -504, 123, -312, 213]) == [-504, 123, -312, 213, 405]
    assert order_by_points([45, -54, 99, -99, 27]) == [45, -54, 27, 99, -99]
    assert order_by_points([]) == []
