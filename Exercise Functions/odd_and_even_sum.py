# You will receive a single number. You should write a function that returns the sum of all even
# and all odd digits in a given number. The result should be returned as a single string in the format:
#
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
#
# Print the result of the function on the console.

#            Examples
#
# Input                    Output
#
# 1000435                  Odd sum = 9, Even sum = 4
#
# 3495892137259234         Odd sum = 54, Even sum = 22


def odd_and_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for numbers in num:
        if int(numbers) % 2 == 0:
            even_sum += int(numbers)
        else:
            odd_sum += int(numbers)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()

print(odd_and_even_sum(number))
