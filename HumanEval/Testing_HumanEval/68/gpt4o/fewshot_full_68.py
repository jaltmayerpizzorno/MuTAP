def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]



def test():

    assert pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    assert pluck([1, 3, 5, 7, 9]) == []
    assert pluck([4, 3, 2, 1]) == [2, 2]
    assert pluck([]) == []
    assert pluck([10, 15, 20, 25, 30]) == [10, 0]
    assert pluck([3, 5, 7, 2, 2, 8]) == [2, 3] # This will help identify if the function correctly returns the first occurrence of the smallest even number

    assert pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    assert pluck([1, 3, 5, 7, 9]) == []
    assert pluck([4, 3, 2, 1]) == [2, 2]
    assert pluck([]) == []
    assert pluck([10, 15, 20, 25, 30]) == [10, 0]
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]  # New test case to catch fault

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"

    assert pluck([4, 2, 0, 3, 0]) == [0, 2]
    assert pluck([1, 2, 3, 4, 2]) == [2, 1]
    assert pluck([2, 2, 2, 2]) == [2, 0]
    assert pluck([3, 3, 3, 3]) == []
    assert pluck([5, 1, 6, 7, 6, 0]) == [0, 5]

    assert pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    assert pluck([1, 3, 5, 7, 9]) == []
    assert pluck([4, 3, 2, 1]) == [2, 2]
    assert pluck([]) == []
    assert pluck([10, 15, 20, 25, 30]) == [10, 0]
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

