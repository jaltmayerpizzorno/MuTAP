def can_arrange(arr):
    
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind



def test():
        assert can_arrange([1, 5, 3, 4, 2, 6]) == 4
#</test>
