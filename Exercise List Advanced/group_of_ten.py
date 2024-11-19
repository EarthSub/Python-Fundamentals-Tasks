# Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
# and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".

# Examples:
# · The numbers 2, 8, 4, and 10 fall into the group of 10's.
# · The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.

# Hints
#
# · Keep track of the group using a variable to store its max value.
# · Create a loop and filter the elements that are less than or equal to the group boundary and remove them from the original list.
# · Increase the boundary by 10.
# · Loop until the given list is empty.
#


#                         Example

# Input                                               Output

# 8, 12, 38, 3, 17, 19, 25, 35, 50                    Group of 10's: [8, 3]
#                                                     Group of 20's: [12, 17, 19]
#                                                     Group of 30's: [25]
#                                                     Group of 40's: [38, 35] Group of 50's: [50]

# 1, 3, 3, 4, 34, 35, 25, 21, 33                      Group of 10's: [1, 3, 3, 4]
#                                                     Group of 20's: []
#                                                     Group of 30's: [25, 21]
#                                                     Group of 40's: [34, 35, 33]





numbers = list(map(int, input().split(", ")))
group = 10

while numbers:
    current_group = [number for number in numbers if number <= group]
    numbers = [num for num in numbers if num not in current_group]
    print(f"Group of {group}'s: {current_group}")
    group += 10