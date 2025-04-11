def minSubArraySum(nums):
    
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum


def test():
    assert minSubArraySum([1, -2, 3, 10, -4, 7, 2, -5]) == -5
    assert minSubArraySum([2, 3, -4, -1, -2, -1, -5, -3]) == -16
    assert minSubArraySum([-2, -3, -4, -1, -2, -1, -5, -4]) == -22
    assert minSubArraySum([1, 2, 3, 4, 5]) == 1
    assert minSubArraySum([0, -1, -2, -3, -4]) == -10, "Test case 5 failed"
    assert minSubArraySum([]) == 0, "Test case 6 failed"