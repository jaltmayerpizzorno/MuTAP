from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
   return [x for x in strings if substring not in x]
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [x for x in strings if substring in x]


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


