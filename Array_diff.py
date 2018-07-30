# 6 kyu / Array.diff
# Details:
#   Your goal in this kata is to implement a difference function, which subtracts one list from another and returns
#   the result.
#   It should remove all values from list a, which are present in list b.
#   array_diff([1,2],[1]) == [2]
#   If a value is present in b, all of its occurrences must be removed from the other:
#   array_diff([1,2,2,2,3],[2]) == [1,3]
#   https://www.codewars.com/kata/array-dot-diff


def array_diff(a, b):
    return [x for x in a if x not in b]


print(array_diff([1, 2, 2, 2, 4, 3], [2, 3, 2]))
