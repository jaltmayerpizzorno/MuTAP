def can_arrange(arr):
    
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind

def test():
    assert can_arrange([1, 2, 3, 4, 5]) == -1
    assert can_arrange([5, 4, 3, 2, 1]) == 1
    assert can_arrange([1, 3, 2, 4, 5]) == 2
    assert can_arrange([10, 20, 30, 25, 40]) == 3
    assert can_arrange([100, 200, 150, 300]) == 2
    assert can_arrange([1, 2, 3, 4, 3, 6]) == 4
