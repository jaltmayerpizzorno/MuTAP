def total_match(lst1, lst2):
   
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2



def test():

    assert total_match(["a", "bc", "def"], ["ghij", "klm"]) == ["a", "bc", "def"]
    assert total_match(["a", "bc"], ["defg", "hij"]) == ["a", "bc"]
    assert total_match(["abcd"], ["ef", "gh"]) == ['abcd']
    assert total_match(["a", "b", "c"], ["d", "e", "f"]) == ["a", "b", "c"]
    assert total_match([], ["d", "e", "f"]) == []
    assert total_match(["a", "b", "c"], []) == []
    assert total_match([], []) == []
    assert total_match(["a", "bc", "def"], ["ghij", "klm"]) == ["a", "bc", "def"]
    assert total_match(["a", "bc"], ["defg", "hij"]) == ["a", "bc"]
    assert total_match(["abcd"], ["ef", "gh"]) == ['abcd']
    assert total_match(["a", "b", "c"], ["d", "e", "f"]) == ["a", "b", "c"]
    assert total_match([], ["d", "e", "f"]) == []
    assert total_match(["a", "b", "c"], []) == []
    assert total_match([], []) == []
    assert total_match(["a", "bc"], ["def", "ghij"]) == ["a", "bc"]
    assert total_match(["abcd"], ["efg", "hi"]) == ["efg", "hi"]

    assert total_match(["a", "bc", "def"], ["ghij", "klm"]) == ["a", "bc", "def"]
    assert total_match(["a", "bc"], ["defg", "hij"]) == ["a", "bc"]
    assert total_match(["abcd"], ["ef", "gh"]) == ['abcd']
    assert total_match(["a", "b", "c"], ["d", "e", "f"]) == ["a", "b", "c"]
    assert total_match([], ["d", "e", "f"]) == []
    assert total_match(["a", "b", "c"], []) == []
    assert total_match([], []) == []
    assert total_match(["hi", "admin"], ["hI", "Hi"]) == ["hi", "admin"]  # This would previously fail

    assert total_match(["a", "bc", "def"], ["ghij", "klm"]) == ["a", "bc", "def"]
    assert total_match(["a", "bc"], ["defg", "hij"]) == ["a", "bc"]
    assert total_match(["abcd"], ["ef", "gh"]) == ['abcd']
    assert total_match(["a", "b", "c"], ["d", "e", "f"]) == ["a", "b", "c"]
    assert total_match([], ["d", "e", "f"]) == []
    assert total_match(["a", "b", "c"], []) == []
    assert total_match([], []) == []
    assert total_match(["hi", "admin"], ["hI", "Hi"]) == ["hi", "admin"]
    assert total_match(["hi", "admin"], ["hI", "hi", "hi"]) == ["hI", "hi", "hi"]
    assert total_match(["4"], ["1", "2", "3", "4", "5"]) == ["4"]

    assert total_match(["a", "bc", "def"], ["ghij", "klm"]) == ["a", "bc", "def"]
    assert total_match(["a", "bc"], ["defg", "hij"]) == ["a", "bc"]
    assert total_match(["abcd"], ["ef", "gh"]) == ['abcd']
    assert total_match(["a", "b", "c"], ["d", "e", "f"]) == ["a", "b", "c"]
    assert total_match([], ["d", "e", "f"]) == []
    assert total_match(["a", "b", "c"], []) == []
    assert total_match([], []) == []
    assert total_match(["a", "bb"], ["ccc"]) == ["a", "bb"]

    assert total_match(["a", "bc", "def"], ["ghij", "klm"]) == ["a", "bc", "def"]
    assert total_match(["a", "bc"], ["defg", "hij"]) == ["a", "bc"]
    assert total_match(["abcd"], ["ef", "gh"]) == ['abcd']
    assert total_match(["a", "b", "c"], ["d", "e", "f"]) == ["a", "b", "c"]
    assert total_match([], ["d", "e", "f"]) == []
    assert total_match(["a", "b", "c"], []) == []
    assert total_match([], []) == []
    assert total_match(["hi", "admin"], ["hi", "hi", "admin", "project"]) == ["hi", "admin"]
    assert total_match(["hi", "admin"], ["hI", "Hi"]) == ["hi", "admin"]
    assert total_match(["hi", "admin"], ["hI", "hi", "hi"]) == ["hI", "hi", "hi"]
    assert total_match(["4"], ["1", "2", "3", "4", "5"]) == ["4"]

