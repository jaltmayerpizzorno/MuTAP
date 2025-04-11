def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]


def test():
    assert compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert compare([5, 10, 15], [0, 0, 0]) == [5, 10, 15]
    assert compare([10, 20, 30], [10, 20, 30]) == [0, 0, 0]
    assert compare([1, 0, 1], [1, 1, 1]) == [0, 1, 0]
    assert compare([7, 8, 9], [4, 5, 6]) == [3, 3, 3]
