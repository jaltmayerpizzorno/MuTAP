def get_row(lst, x):
    
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])


def test():
    assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]
    assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 7) == [(2, 0)]
    assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 7]], 7) == [(2, 2), (2, 0)]
    assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10) == []
    assert get_row([[1, 2, 3], [4, 2, 6], [2, 8, 9]], 2) == [(0, 1), (1, 1), (2, 0)]
