def by_length(arr):
    
    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except:
            pass
    return new_arr

def test():
    assert by_length([1, 3, 2, 4]) == ["Four", "Three", "Two", "One"]
    assert by_length([9, 7, 5, 3, 1]) == ["Nine", "Seven", "Five", "Three", "One"]
    assert by_length([2, 2, 2]) == ["Two", "Two", "Two"]
    assert by_length([10, 11]) == []
    assert by_length([]) == []
    assert by_length([4, 8, 6]) == ["Eight", "Six", "Four"]

test()
