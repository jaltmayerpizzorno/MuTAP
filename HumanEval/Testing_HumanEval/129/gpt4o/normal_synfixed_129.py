def minPath(grid, k):
    
    n = len(grid)
    val = n * n + 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                temp = []
                if i != 0:
                    temp.append(grid[i - 1][j])

                if j != 0:
                    temp.append(grid[i][j - 1])

                if i != n - 1:
                    temp.append(grid[i + 1][j])

                if j != n - 1:
                    temp.append(grid[i][j + 1])

                val = min(temp)

    ans = []
    for i in range(k):
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)
    return ans

def test():
    # Test when grid is 3x3 and k=4
    grid = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    k = 4
    assert minPath(grid, k) == [1, 0, 1, 0]

    # Test when grid is 3x3 and k=5
    grid = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    k = 5
    assert minPath(grid, k) == [1, 0, 1, 0, 1]

    # Test when grid is 2x2 and k=3
    grid = [
        [0, 1],
        [1, 0]
    ]
    k = 3
    assert minPath(grid, k) == [1, 0, 1]

    # Test when grid is 1x1 and k=1
    grid = [
        [1]
    ]
    k = 1
    assert minPath(grid, k) == [1]
    
    # Test when grid is 3x3 and k=2 with all zeros
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    k = 2
    assert minPath(grid, k) == [1, 9]  # Since the initial val is 10 (n*n + 1)

test()
