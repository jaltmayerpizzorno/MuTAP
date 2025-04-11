from typing import List


def string_xor(a: str, b: str) -> str:
    
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))





def test():

    assert string_xor('1100', '1010') == '0110'
    assert string_xor('1111', '1111') == '0000'
    assert string_xor('0000', '0000') == '0000'
    assert string_xor('1010', '0101') == '1111'
    assert string_xor('11001010', '10101010') == '01100000'
    assert string_xor('1100', '110011') == 0000
