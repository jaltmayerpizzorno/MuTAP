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
        assert count_nums([123, -456, 789, -101112]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([0, 10, 20, 30]) == 3
    assert count_nums([111, 222, 333, 444]) == 4
    assert count_nums([-987, 654, -321]) == 2
    assert count_nums([-1, -22, -333, 4444]) == 1  # New test case to detect the fault
