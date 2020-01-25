#
# Write a function that merges two sorted arrays into a single one. The arrays only contain integers.
# Also, the final outcome must be sorted and not have any duplicate.


def merge_arrays(first, second):
    mergedlist = list(set(first + second))
    mergedlist.sort()
    return mergedlist
    pass

print(merge_arrays([1, 3, 5], [2, 4, 6]))
print(merge_arrays([2, 4, 8], [2, 4, 6]))