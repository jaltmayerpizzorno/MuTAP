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
    assert fib4(5) == 2
    assert fib4(6) == 4
    assert fib4(7) == 8
    assert fib4(8) == 16
    assert fib4(9) == 30
    assert fib4(10) == 60

test()
