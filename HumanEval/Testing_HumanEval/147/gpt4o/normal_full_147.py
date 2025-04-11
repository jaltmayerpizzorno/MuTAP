def get_max_triples(n):
    
    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += [(A[i],A[j],A[k])]
    return len(ans)



def test():

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(12) == 84

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(11) == 45  # New test case to detect fault

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(11) == 55  # New test case to detect the fault

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(15) == 136

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(100) == 7058  # New test case to detect the fault

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(20) == 374

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(11) == 36
    assert get_max_triples(12) == 46
    assert get_max_triples(13) == 63
    assert get_max_triples(14) == 78
    assert get_max_triples(15) == 87

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(0) == 0  # New test case to detect fault in code snippet
    assert get_max_triples(3) == 0  # Another edge case

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(100) == 166650

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(11) == 38
    assert get_max_triples(12) == 57
    assert get_max_triples(13) == 86
    assert get_max_triples(14) == 116
    assert get_max_triples(15) == 158

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(11) == 45  # This value should help detect the faulty code change

    assert get_max_triples(11) == 45
    assert get_max_triples(12) == 61
    assert get_max_triples(13) == 85

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(11) == 38  # Example: triples (1, 7, 13), (1, 13, 19), etc.

    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 4
    assert get_max_triples(7) == 10
    assert get_max_triples(8) == 11
    assert get_max_triples(9) == 21
    assert get_max_triples(10) == 36
    assert get_max_triples(11) == 55
    assert get_max_triples(12) == 77

