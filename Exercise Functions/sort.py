# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().

#             Example
#
# Input                       Output
#
# 6 2 4                       [2, 4, 6]
#
# 12 52 11 53 2 8 45          [2, 8, 11, 12, 45, 52, 53]



def sorted_list(item: list) -> list:
    return sorted(item)


list_as_string = input().split()
list_as_integers = [int(num) for num in list_as_string]

print(sorted_list(list_as_integers))