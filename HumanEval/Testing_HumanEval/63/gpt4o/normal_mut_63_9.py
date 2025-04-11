def fibfib(n: int):
    
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)





def test():
        assert fibfib(0) == 0
    assert fibfib(1) == 0
    assert fibfib(2) == 1
    assert fibfib(3) == 1
    assert fibfib(4) == 2
    assert fibfib(5) == 4
    assert fibfib(6) == 7
    assert fibfib(7) == 13
    assert fibfib(8) == 24  # Adding a test case for n=8 to detect the fault in the previous code
    assert fibfib(9) == 44  # Adding another test case for n=9
