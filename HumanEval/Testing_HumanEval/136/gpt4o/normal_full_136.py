def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)



def test():

    assert largest_smallest_integers([3, -1, -2, 5, -4, 6]) == (-1, 3)
    assert largest_smallest_integers([-10, -20, -30]) == (-10, None)
    assert largest_smallest_integers([10, 20, 30]) == (None, 10)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([-1, 1]) == (-1, 1)
    assert largest_smallest_integers([0, 0, 0]) == (None, None)
    assert largest_smallest_integers([3, -1, -2, 5, -4, 6]) == (-1, 3)
    assert largest_smallest_integers([-10, -20, -30]) == (-10, None)
    assert largest_smallest_integers([10, 20, 30]) == (None, 10)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([-1, 1]) == (-1, 1)
    assert largest_smallest_integers([0, 0, 0]) == (None, None)
    assert largest_smallest_integers([1, 0, -1]) == (-1, 1)

    assert largest_smallest_integers([3, -1, -2, 5, -4, 6]) == (-1, 3)
    assert largest_smallest_integers([-10, -20, -30]) == (-10, None)
    assert largest_smallest_integers([10, 20, 30]) == (None, 10)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([-1, 1]) == (-1, 1)
    assert largest_smallest_integers([0, 0, 0]) == (None, None)
    assert largest_smallest_integers([0, -5, 5, 0]) == (-5, 5)

    assert largest_smallest_integers([3, -1, -2, 5, -4, 6]) == (-1, 3)
    assert largest_smallest_integers([-10, -20, -30]) == (-10, None)
    assert largest_smallest_integers([10, 20, 30]) == (None, 10)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([-1, 1]) == (-1, 1)
    assert largest_smallest_integers([0, 0, 0]) == (None, None)
    assert largest_smallest_integers([-3, 0, 5]) == (-3, 5)

    assert largest_smallest_integers([1, -1, -2, 2, -3, 3, 0]) == (-1, 1)
    assert largest_smallest_integers([3, -1, -2, 5, -4, 6]) == (-1, 3)
    assert largest_smallest_integers([-10, -20, -30]) == (-10, None)
    assert largest_smallest_integers([10, 20, 30]) == (None, 10)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([-1, 1]) == (-1, 1)
    assert largest_smallest_integers([0, 0, 0]) == (None, None)

