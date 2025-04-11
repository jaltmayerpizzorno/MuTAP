def get_row(lst, x):
    
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])



def test():
        assert get_row([[1, 2, 3, 1], [4, 1, 6, 1], [1, 8, 9, 1]], 1) == [(0, 3), (0, 0), (1, 3), (1, 1), (2, 3), (2, 0)]
    assert get_row([[1, 2, 3], [4, 1, 6], [1, 8, 1]], 1) == [(0, 0), (1, 1), (2, 2), (2, 0)]
