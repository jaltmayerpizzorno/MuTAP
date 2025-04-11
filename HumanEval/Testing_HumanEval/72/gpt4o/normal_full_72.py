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

    # Test case 1: sum(q) <= w and q is a palindrome    q = [1, 2, 3, 2, 1]    w = 10    assert will_it_fly(q, w) == True