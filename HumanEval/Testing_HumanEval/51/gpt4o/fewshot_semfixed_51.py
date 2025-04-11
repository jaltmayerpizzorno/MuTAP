def remove_vowels(text):
    
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])




def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"    assert triangle(2, 2, 3) == "Isosceles triangle"    assert triangle(2, 3, 4) == "Scalene triangle"