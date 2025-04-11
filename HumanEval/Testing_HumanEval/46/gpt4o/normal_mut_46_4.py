def fib4(n: int):
    
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]





def test():
        assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28
    assert fib4(9) == 54
    assert fib4(10) == 104
    # New test cases to detect faults
    assert fib4(11) == 200
    assert fib4(12) == 384
    assert fib4(13) == 740
    assert fib4(14) == 1428
    assert fib4(15) == 2756
    assert fib4(16) == 5320
    assert fib4(17) == 10252
    assert fib4(18) == 19756
    assert fib4(19) == 38056
    assert fib4(20) == 73384

test()
