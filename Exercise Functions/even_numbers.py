# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().

#           Example
#
# Input                Output
#
# 1 2 3 4              [2, 4]
#
# 1 2 3 -1 -2 -3       [2, -2]



def is_even(list_of_int: int) -> int:
    return list_of_int % 2 == 0


list_as_string = input().split()
list_as_integers = [int(num) for num in list_as_string]

even_list = []

for num in list_as_integers:
    if is_even(num):
        even_list.append(num)

print(even_list)
