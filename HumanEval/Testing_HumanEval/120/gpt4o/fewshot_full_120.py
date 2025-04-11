def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans



def test():

    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"