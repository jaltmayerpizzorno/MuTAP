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
    assert count_nums([123, -456, 789, -101112]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([0, 10, 20, 30]) == 3
    assert count_nums([111, 222, 333, 444]) == 4
    assert count_nums([-987, 654, -321]) == 2
    assert count_nums([-10, -20, -30]) == 0

    assert count_nums([123, -456, 789, -101112]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([0, 10, 20, 30]) == 3
    assert count_nums([111, 222, 333, 444]) == 4
    assert count_nums([-987, 654, -321]) == 2
    assert count_nums([-10, -20, -30, -40]) == 0  # New test case to detect the issue with n[0] being divided instead of multiplied

    assert count_nums([123, -456, 789, -101112]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([0, 10, 20, 30]) == 3
    assert count_nums([111, 222, 333, 444]) == 4
    assert count_nums([-987, 654, -321]) == 2
    assert count_nums([-100, -200, -300, -400, -500, 600]) == 1  # New test case

    assert count_nums([123, -456, 789, -101112]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([0, 10, 20, 30]) == 3
    assert count_nums([111, 222, 333, 444]) == 4
    assert count_nums([-987, 654, -321]) == 2
    assert count_nums([-1, 11, -11]) == 1  # New test case that detects the fault
    assert count_nums([1, 1, 2]) == 3  # New test case that detects the fault

    assert count_nums([1, -2, 30, -40]) == 2
    assert count_nums([-10, 20, -30, 40]) == 1
    assert count_nums([-1, -1, -1, 1]) == 1
    assert count_nums([1001, -1001, 1001, -1001]) == 2
    assert count_nums([0, -10, 10, -20, 20]) == 2

    assert count_nums([123, -456, 789, -101112]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([0, 10, 20, 30]) == 3
    assert count_nums([111, 222, 333, 444]) == 4
    assert count_nums([-987, 654, -321]) == 2
    assert count_nums([-10, 10, -20, 20]) == 2  # New test case to detect the fault

    assert count_nums([1, -1, 10, -10]) == 2
    assert count_nums([0, -1, -9]) == 0
    assert count_nums([123, -321, 456, -654]) == 2
    assert count_nums([555, -555, 0, 111, -111]) == 3
    assert count_nums([99, -99, 88, -88, 77, -77]) == 3

    assert count_nums([123, -456, 789, -101112]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([0, 10, 20, 30]) == 3
    assert count_nums([111, 222, 333, 444]) == 4
    assert count_nums([-987, 654, -321]) == 2
    assert count_nums([0, -10, 20, -30]) == 2  # new test case to catch the fault

    assert count_nums([0, -10, 20, -30]) == 1

    assert count_nums([123, -456, 789, -101112]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([0, 10, 20, 30]) == 3
    assert count_nums([111, 222, 333, 444]) == 4
    assert count_nums([-987, 654, -321]) == 2
    assert count_nums([1, -10, 100, -1000, 10000]) == 4
    assert count_nums([-111, -222, -333, -444]) == 0
    assert count_nums([-5, 5, -15, 15]) == 2
    assert count_nums([999, -999, 99, -99]) == 2
    assert count_nums([0, -0, 1, -1]) == 1

    assert count_nums([100, -200, 300, -400]) == 3
    assert count_nums([0, -1, 2, -3, 4, -5]) == 2
    assert count_nums([1234, -4321, 5678, -8765]) == 3
    assert count_nums([-10, 20, -30, 40]) == 2
    assert count_nums([-1111, 2222, -3333, 4444]) == 2

    assert count_nums([123, -456, 789, -101112]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([0, 10, 20, 30]) == 3
    assert count_nums([111, 222, 333, 444]) == 4
    assert count_nums([-987, 654, -321]) == 2
    assert count_nums([-11, -22, -33]) == 0  # New test case to check for negative sums

    assert count_nums([123, -456, 789, -101112]) == 4
    assert count_nums([-1, -2, -3, -4, -5]) == 0
    assert count_nums([0, 10, 20, 30]) == 3
    assert count_nums([111, 222, 333, 444]) == 4
    assert count_nums([-987, 654, -321]) == 2
    assert count_nums([-1, -22, -333, 4444]) == 1  # New test case to detect the fault

