def string_to_md5(text):
    
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

def test():
    assert string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert string_to_md5("world") == "fc3ff98e8c6a0d3087d515c0473f8677"
    assert string_to_md5("") == None
    assert string_to_md5("123") == "202cb962ac59075b964b07152d234b70"
    assert string_to_md5(None) == None
