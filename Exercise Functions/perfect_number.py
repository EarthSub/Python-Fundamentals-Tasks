# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
#
# Write a function that receives an integer number and returns one of the following messages:
#
# · "We have a perfect number!" - if the number is perfect.
#
# · "It's not so perfect." - if the number is NOT perfect.
#
# Print the result on the console.

                # Examples
#
# Input           Output                          Comments
#
# 6               We have a perfect number!       1 + 2 + 3
#
# 28              We have a perfect number!       1 + 2 + 4 + 7 + 14
#
# 1236498         It's not so perfect.





def perfect_number(n: int) -> str:
    sum_of_numbers = 0
    for num in range(1, n):
        if n % num == 0:
            sum_of_numbers += num
    if n == sum_of_numbers:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(perfect_number(number))