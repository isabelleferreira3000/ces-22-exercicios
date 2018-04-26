import sys
import string


def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def cleanword(word):
    change = True
    while change:
        if remove_punctuation(word) == word:
            change = False
        else:
            word = remove_punctuation(word)
    return word


def has_dashdash(word):
    if "--" in word:
        return True
    else:
        return False


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct


def extract_words(phrase):
    change = True
    while change:
        if remove_punctuation(phrase) == phrase:
            change = False
        else:
            phrase = remove_punctuation(phrase)

    words = phrase.split()
    words_2 = []
    for i in words:
        words_2.append(i.lower())

    return words_2


def wordcount(word, list_of_words):
    count = 0
    for i in list_of_words:
        if i == word:
            count += 1
    return count


def wordset(list_of_words):
    list_clean = []
    for i in list_of_words:
        if i not in list_clean:
            list_clean.append(i)

    list_clean.sort()
    return list_clean


def longestword(list_of_words):
    maximo = 0
    for i in list_of_words:
        if maximo < len(i):
            maximo = len(i)

    return maximo


test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") == "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time! 'Now', is the time? Yes, now.") ==
     ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
     ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])

test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this", "supercalifragilisticexpialidocious"]) == 34)
test(longestword([]) == 0)