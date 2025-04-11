def how_many_times(string: str, substring: str) -> int:
    
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times





def test():
        assert how_many_times("abababa", "aba") == 3
    assert how_many_times("aaaaa", "aa") == 4
    assert how_many_times("hello world", "l") == 3
    assert how_many_times("abc", "d") == 0
    assert how_many_times("aaaa", "aaaa") == 1
    assert how_many_times("", "a") == 0
    assert how_many_times("a", "") == 2
    assert how_many_times("", "") == 1
    assert how_many_times("aabbaabb", "aabb") == 2  # New test case to detect the fault
