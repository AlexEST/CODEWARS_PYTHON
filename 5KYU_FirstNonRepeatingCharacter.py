"""
Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
"""


def first_non_repeating_letter(string):
    arr = []
    lowString = string.lower()
    for i in range(0, len(string)):
        if string[i] not in arr:
            if lowString.find(string[i].lower(), i + 1, len(string)) == -1:
                return string[i]
        arr.append(string[i])
    return ""


print(first_non_repeating_letter("sTress"))
print(first_non_repeating_letter("moonmen"))
print(first_non_repeating_letter("sTreSS"))
print(first_non_repeating_letter("abba"))