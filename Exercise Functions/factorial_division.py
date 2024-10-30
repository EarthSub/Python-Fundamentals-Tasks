# Write a function that receives two integer numbers. Calculate the factorial of each number.

# Divide the first result by the second and print the division formatted to the second decimal point.

#       Examples

# Input           Output

# 5               60.00
# 2

# 6               360.00
# 2




def first_factorial(number: int) -> float:
    factorial_one = 1
    for num in range(number, 1, -1):
        factorial_one *= num
    return factorial_one


def second_factorial(number: int) -> float:
    factorial_two = 1
    for num in range(number, 1, -1):
        factorial_two *= num
    return factorial_two


def factorial_division():
    result = first_factorial(first_number) / second_factorial(second_number)
    return f"{result:.2f}"


first_number = int(input())
second_number = int(input())

print(factorial_division())