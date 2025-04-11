def will_it_fly(q,w):
   
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True

def test():
    # Test case 1: sum(q) <= w and q is a palindrome
    q = [1, 2, 3, 2, 1]
    w = 10
    assert will_it_fly(q, w) == True

    # Test case 2: sum(q) > w
    q = [1, 2, 3, 2, 1]
    w = 8
    assert will_it_fly(q, w) == False

    # Test case 3: sum(q) <= w but q is not a palindrome
    q = [1, 2, 3, 4, 5]
    w = 20
    assert will_it_fly(q, w) == False

    # Test case 4: q is an empty list
    q = []
    w = 0
    assert will_it_fly(q, w) == True

    # Test case 5: q has one element
    q = [5]
    w = 5
    assert will_it_fly(q, w) == True
