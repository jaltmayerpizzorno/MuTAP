def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]


def test():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    assert compare([1, 2, 3], [1, 2, 4]) == [0, 0, 1]
    assert compare([10, 20, 30], [5, 15, 25]) == [5, 5, 5]
    assert compare([1, 1, 1], [2, 2, 2]) == [1, 1, 1]
