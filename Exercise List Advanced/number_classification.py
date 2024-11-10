# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
# and prints all the positive, negative, even, and odd numbers on separate lines as shown below.

# Note: Zero is counted as a positive number


#                              Examples

# Input                                                   Output

# 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33               Positive: 1, 0, 5, 3, 4, 12, 19
#                                                         Negative: -2, -100, -20, -33
#                                                         Even: -2, 0, 4, -100, -20, 12 Odd: 1, 5, 3, 19, -33


# 1, 2, 53, 2, 21 Positive: 1, 2, 53, 2, 21 Negative:     Even: 2, 2 Odd: 1, 53, 21



def positive_numbers(x):
    positive = [num for num in x if num >= 0]
    return ", ".join(map(str, positive))


def negative_numbers(x):
    negative = [num for num in x if num < 0]
    return ", ".join(map(str, negative))


def even_numbers(x):
    even = [num for num in x if num % 2 == 0]
    return ", ".join(map(str, even))


def odd_numbers(x):
    odd = [num for num in x if num % 2 == 1]
    return ", ".join(map(str, odd))


numbers_as_list = list(map(int, input().split(", ")))

print(f"Positive: {positive_numbers(numbers_as_list)}")
print(f"Negative: {negative_numbers(numbers_as_list)}")
print(f"Even: {even_numbers(numbers_as_list)}")
print(f"Odd: {odd_numbers(numbers_as_list)}")