# You will receive three integer numbers.
#
# Write functions named:
#
# · sum_numbers() that returns the sum of the first two integers
#
# · subtract() that returns the difference between the returned result of the first function and the third integer
#
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.

#          Examples
#
# Input                Output
#
#   23
#   6                    19
#   10
#
#   1
#   17                   -12
#   30
#
#   42
#   58                   0
#   100
#
#
#


def sum_numbers(first_number: int, second_number: int) -> int:
    sum_of_numbers = first_number + second_number
    return sum_of_numbers


def subtract(third_number: int, fourth_number: int) -> int:
    subtracted_number = third_number - fourth_number
    return subtracted_number


def add_and_subtract(first: int, second: int, third: int) -> int:
    result = subtract(sum_numbers(num_one, num_two), num_three)
    return result


num_one = int(input())
num_two = int(input())
num_three = int(input())

print(add_and_subtract(num_one, num_two, num_three))
