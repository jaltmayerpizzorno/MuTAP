def can_arrange(arr):
    
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind



def test():
        assert can_arrange([1, 2, 3, 4, 2, 5, 6]) == 4
    assert can_arrange([1, 2, 3, 4, 5, 6]) == -1
    assert can_arrange([6, 5, 4, 3, 2, 1]) == 5
    assert can_arrange([1, 3, 2, 4, 5, 6]) == 2
    assert can_arrange([1]) == -1
    assert can_arrange([1, 2, 3, 4, 5, 3, 6]) == 5
#</test>
