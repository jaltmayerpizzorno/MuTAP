from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
        result.append(string[:])

    for i in range(len(string)):
        result.append(string[:i+1])
    return result


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}

print(all_prefixes('abcde') == ['', 'a', 'ab', 'abc', 'abcd', 'abcde'])


