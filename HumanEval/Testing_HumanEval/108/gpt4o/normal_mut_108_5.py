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
        assert count_nums([100, -200, 300, -400]) == 3
    assert count_nums([0, -1, 2, -3, 4, -5]) == 2
    assert count_nums([1234, -4321, 5678, -8765]) == 3
    assert count_nums([-10, 20, -30, 40]) == 2
    assert count_nums([-1111, 2222, -3333, 4444]) == 2
