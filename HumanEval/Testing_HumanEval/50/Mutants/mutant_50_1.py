def encode_shift(s: str):
    """
   return ''.join([chr((((ord(ch) + 5) + ord('a')) % 26) + ord('a')) for ch in s])
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


METADATA = {}


