def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)



def test():

    assert is_bored("I am bored. You are not. I am still bored!") == 2
    assert is_bored("I am happy. You are sad. It is raining outside.") == 1
    assert is_bored("This is a test. I am testing. Still testing? Yes, I am.") == 1
    assert is_bored("Why are you bored? I don't understand.") == 1
    assert is_bored("") == 0
    assert is_bored("No sentence starts with I here.") == 0
    assert is_bored("I. I! I?") == 0
    assert is_bored("I am bored. You are not. I am still bored!") == 2
    assert is_bored("I am happy. You are sad. It is raining outside.") == 1
    assert is_bored("This is a test. I am testing. Still testing? Yes, I am.") == 1
    assert is_bored("Why are you bored? I don't understand.") == 1
    assert is_bored("") == 0
    assert is_bored("No sentence starts with I here.") == 0
    assert is_bored("I. I! I?") == 0
    assert is_bored("I am. I need. I want. I love.") == 4  # New test case to catch the fault

    assert is_bored("I am bored. You are not. I am still bored!") == 2
    assert is_bored("I am happy. You are sad. It is raining outside.") == 1
    assert is_bored("This is a test. I am testing. Still testing? Yes, I am.") == 1
    assert is_bored("Why are you bored? I don't understand.") == 1
    assert is_bored("") == 0
    assert is_bored("No sentence starts with I here.") == 0
    assert is_bored("I. I! I?") == 0
    assert is_bored("I am bored. You are bored. I am still bored!") == 2

    assert is_bored("I am bored. You are not. I am still bored!") == 2
    assert is_bored("I am happy. You are sad. It is raining outside.") == 1
    assert is_bored("This is a test. I am testing. Still testing? Yes, I am.") == 1
    assert is_bored("Why are you bored? I don't understand.") == 1
    assert is_bored("") == 0
    assert is_bored("No sentence starts with I here.") == 0
    assert is_bored("I. I! I?") == 0
    assert is_bored("I.I!I?") == 3  # Should be 3 boredoms since each "I" is considered a sentence

