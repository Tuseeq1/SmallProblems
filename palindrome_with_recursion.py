"""
I was asked this questing in my first job interview as fresh graduates, its actually very simple
but just wanted to add this as well

write a method to find if a sequence is palindrome or not, using recursion

a palindrome is a sequence that is same if read backwards e-g 'abba', or 'madam'
"""


def is_palindrome(seq):
    if len(seq) < 2:
        return True
    if seq[0] != seq[-1]:
        return False
    return is_palindrome(seq[1:-1])


assert is_palindrome('madam') is True
assert is_palindrome('abba') is True
assert is_palindrome([1, 2, 0, 2, 1]) is True
assert is_palindrome([1, 2, 3, 0, 2, 1]) is False
assert is_palindrome('anything') is False
assert is_palindrome('rerunner') is False
