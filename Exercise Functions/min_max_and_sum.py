# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().
#
# The output should be as follows:
#
# · On the first line: "The minimum number is {minimum number}"
#
# · On the second line: "The maximum number is {maximum number}"
#
# · On the third line: "The sum number is: {sum of all numbers}"


#               Example

# Input                           Output
#
#                                 The minimum number is 2
# 2 4 6                           The maximum number is 6
#                                 The sum number is: 12
#
#                                 The minimum number is 2
# 12 52 11 53 2 5 45              The maximum number is 53
#                                 The sum number is: 183


def min_num(minimum: list) -> print:
    minimum_number = min(minimum)
    print(f"The minimum number is {minimum_number}")


def max_num(maximum: list) -> print:
    maximum_number = max(maximum)
    print(f"The maximum number is {maximum_number}")


def sum_num(total_sum: list) -> print:
    sum_numbers = sum(total_sum)
    print(f"The sum number is: {sum_numbers}")


list_as_string = input().split()
list_as_integers = [int(num) for num in list_as_string]

min_num(list_as_integers)
max_num(list_as_integers)
sum_num(list_as_integers)
