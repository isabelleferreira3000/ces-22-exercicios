import sys


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def reverse(word):
    word_inverse = ""
    ix = -1

    while ix >= -len(word):
        word_inverse += word[ix]
        ix -= 1
    return word_inverse


def is_palindrome(word):
    word_inverse = reverse(word)
    if word == word_inverse:
        return True
    return False


test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))
