def move_one_ball(arr):
    
    if len(arr)==0:
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=arr.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      if my_arr[i]!=sorted_array[i]:
        return False
    return True



def test():
        assert move_one_ball([3, 4, 5, 1, 2]) == True, "Test case 1 failed"
    assert move_one_ball([1, 2, 3, 4, 5]) == True, "Test case 2 failed"
    assert move_one_ball([2, 3, 4, 5, 1]) == True, "Test case 3 failed"
    assert move_one_ball([4, 1, 2, 3, 5]) == False, "Test case 4 failed"
    assert move_one_ball([]) == True, "Test case 5 failed"
    assert move_one_ball([1]) == True, "Test case 6 failed"
    assert move_one_ball([1, 3, 2]) == False, "Test case 7 failed"
    assert move_one_ball([2, 1]) == True, "Test case 8 failed"
    assert move_one_ball([1, 2, 4, 3, 5]) == False, "Test case 9 failed"  # New test case to detect fault
