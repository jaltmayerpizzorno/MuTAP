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
    assert fib4(11) == 200
    assert fib4(12) == 386
    assert fib4(13) == 744
    assert fib4(14) == 1434
    assert fib4(15) == 2764

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
    assert fib4(11) == 200
    assert fib4(12) == 384
    assert fib4(13) == 736
    assert fib4(14) == 1416
    assert fib4(15) == 2720

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
    assert fib4(11) == 200  # New test case to detect potential fault
    assert fib4(12) == 384  # New test case to detect potential fault

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
    assert fib4(11) == 200  # Check if fib4(11) is correctly calculated
    assert fib4(15) == 2378  # Check if fib4(15) is correctly calculated

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
    assert fib4(11) == 200  # This should detect if results[1] instead of results[-1] is returned

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
    assert fib4(11) == 200  # New test case to detect incorrect behavior
    assert fib4(12) == 384  # Additional test case

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
    assert fib4(11) == 200
    assert fib4(12) == 384

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
    assert fib4(11) == 200
    assert fib4(12) == 384
    assert fib4(13) == 736
    assert fib4(14) == 1416
    assert fib4(15) == 2720
    assert fib4(16) == 5224

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
    assert fib4(11) == 200  # new test case
    assert fib4(12) == 384  # new test case

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
    assert fib4(11) == 200  # Expected value based on the correct fib4 sequence
    assert fib4(12) == 386  # Expected value based on the correct fib4 sequence

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
    assert fib4(20) == 57424
    assert fib4(50) == 796614834
    assert fib4(100) == 3617380915556

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
    assert fib4(11) == 200  # Adding a test case beyond the initial sequence size to check for unexpected 'return results[+1]' behavior

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
    assert fib4(15) == 2768

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
    assert fib4(11) == 200
    assert fib4(12) == 384
    assert fib4(13) == 736
    assert fib4(14) == 1408
    assert fib4(15) == 2704

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
    assert fib4(11) == 200  # new test case to catch the error

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

