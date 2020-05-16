"""
Given a series of numbers as a string, determine if the number represented by the string is divisible by three.

You can expect all test case arguments to be strings representing values greater than 0.

Example:

"123"      -> true
"8409"     -> true
"100853"   -> false
"33333333" -> true
"7"        -> false
"""


def divisible_by_three(st):
    return int(st) % 3 == 0
    pass


print(divisible_by_three("123"))
