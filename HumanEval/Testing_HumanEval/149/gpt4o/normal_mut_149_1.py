def sorted_list_sum(lst):
    
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)



def test():
        assert sorted_list_sum(["apple", "banana", "kiwi", "berry"]) == ['kiwi', 'banana']
    assert sorted_list_sum(["cat", "dog", "elephant", "tiger"]) == ['elephant']
    assert sorted_list_sum(["one", "two", "three", "four", "five", "six"]) == ['five', 'four']
    assert sorted_list_sum(["a", "bb", "ccc", "dddd", "eeeee"]) == ["bb", "dddd"]
    assert sorted_list_sum([]) == []
    assert sorted_list_sum(["single"]) == ['single']
    assert sorted_list_sum(["abcd", "ef", "ghij", "klmno", "pqrstuv"]) == ['ef', 'abcd', 'ghij']
