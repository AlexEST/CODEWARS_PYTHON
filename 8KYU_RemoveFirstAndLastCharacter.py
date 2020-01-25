#
#
# Alexander Chelpanov
# Date: 25.01.2020
#
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
#
#
#
def remove_char(s):
    return s[1:len(s)-1]

print(remove_char('eloquent'))
print(remove_char('country'))
print(remove_char('person'))
print(remove_char('ok'))
