def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]



def test():
        assert pluck([3, 5, 7, 2, 2, 8]) == [2, 3] # This will help identify if the function correctly returns the first occurrence of the smallest even number
#</test>
