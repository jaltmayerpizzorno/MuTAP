def count_nums(arr):
    
    def digits_sum(n):
        neg = 1
        if n < 0: 
            n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))



def test():
        assert count_nums([1, -1, 10, -10]) == 2
    assert count_nums([0, -1, -9]) == 0
    assert count_nums([123, -321, 456, -654]) == 2
    assert count_nums([555, -555, 0, 111, -111]) == 3
    assert count_nums([99, -99, 88, -88, 77, -77]) == 3
