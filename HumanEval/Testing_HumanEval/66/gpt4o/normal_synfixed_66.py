def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)
def test():
    assert digitSum("") == 0
    assert digitSum("a") == 0
    assert digitSum("A") == ord("A")
    assert digitSum("AbC") == ord("A") + ord("C")
    assert digitSum("abc") == 0
    assert digitSum("AbC123") == ord("A") + ord("C")
    assert digitSum("aBcD") == ord("B") + ord("D")

test()
