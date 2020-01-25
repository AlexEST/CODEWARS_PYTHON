# Write a function that rearranges an integer into its largest possible value.
#
# super_size(123456) # 654321
# super_size(105)    # 510
# super_size(12)     # 21
# If the argument passed through is single digit or is already the maximum possible integer,
# your function should simply return it.
#

def super_size(n):
    arr = [i for i in str(n)]
    arr.sort(reverse=True)
    return int(''.join(str(i) for i in arr))


print(super_size(69))
print(super_size(513))
print(super_size(2017))
print(super_size(414))
print(super_size(608719))
