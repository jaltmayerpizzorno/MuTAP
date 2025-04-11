def string_to_md5(text):
    
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

def test():
    assert string_to_md5("test") == "098f6bcd4621d373cade4e832627b4f6"
    assert string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    assert string_to_md5("") == None
    assert string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"
    assert string_to_md5("abcdefg") == "7ac66c0f148de9519b8bd264312c4d64"
#</test>