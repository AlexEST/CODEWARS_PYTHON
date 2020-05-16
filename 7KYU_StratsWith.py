"""
Challenge: Given two null-terminated strings in the arguments "string" and "prefix",
determine if "string" starts with the "prefix" string. Return 1 (or any other "truthy" value) if true, 0 if false.

Example:

startsWith("hello world!", "hello"); // should return 1.
startsWith("hello world!", "HELLO"); // should return 0.
startsWith("nowai", "nowaisir"); // should return 0.
Addendum: For this problem, an empty "prefix" string should always return 1 (true) for any value of "string".

If the length of the "prefix" string is greater than the length of the "string", return 0.
"""


def starts_with(st, prefix):
    if st[:len(prefix)] == prefix:
        return 1
    else:
        return 0


print(starts_with('hello world', 'hello'))
