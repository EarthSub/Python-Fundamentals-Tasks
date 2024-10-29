# A palindrome is a number that reads the same backward as forward,
# such as 323 or 1001. Write a function that receives a list of positive integers,
# separated by comma and space ", ". The function should check if each integer is a palindrome - True or False.
# Print the result.


#                                      Examples
#
# Input                         Output             Input                           Output
#
# 123, 323, 421, 121            False              32, 2, 232, 1010                False
#                               True                                               True
#                               False                                              True
#                               True                                               False


def palindrome(num: str) -> bool:
    return num == num[::-1]


number_as_string = input().split(", ")
for number in number_as_string:
    print(palindrome(number))
