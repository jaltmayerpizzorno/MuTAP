def sorted_list_sum(lst):
    
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)


def test():
    assert sorted_list_sum(["apple", "banana", "kiwi", "cherry", "mango"]) == ['kiwi', 'banana', 'cherry']
    assert sorted_list_sum(["a", "bb", "ccc", "dd", "eeee"]) == ["bb", "dd", "eeee"]
    assert sorted_list_sum(["abcd", "efgh", "ij", "klmno", "pqrstu"]) == ['ij', 'abcd', 'efgh', 'pqrstu']
    assert sorted_list_sum(["one", "three", "five", "seven", "nine"]) == ['five', 'nine']
    assert sorted_list_sum([]) == []
