"""
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once. e-g "table" and "bleat"  or "binary" and "brainy".

This code will check if two string are anagram of each other in O(n1logn1 + n2logn2) worst case
for O(n1+n2) checkout "https://github.com/chiphuyen/coding-exercises/blob/master/anagrams.py"
"""


def are_anagrams_fast(str1, str2):
    if len(str1) != len(str2):
        return False

    if sorted(str1) == sorted(str2):
        return True
    return False


assert are_anagrams_fast('table', 'bleat') is True
assert are_anagrams_fast('table', 'bleate') is False
assert are_anagrams_fast('honey', 'eyhon') is True
assert are_anagrams_fast('bra', 'bar') is True
assert are_anagrams_fast('place', 'palace') is False
assert are_anagrams_fast('', '') is True
