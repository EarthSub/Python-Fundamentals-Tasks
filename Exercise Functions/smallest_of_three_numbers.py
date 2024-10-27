# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console. Use an appropriate name for the function.
#
#             Examples
#
#      Input            Output
#
#        2
#        5                 2
#        3
#
#        600
#        342               123
#        123
#
#        25
#        21                 4
#        4





def smallest_number(number_one: int, number_two: int, number_three: int) -> int:
    return min(number_one, number_two, number_three)



first_number = int(input())
second_number = int(input())
third_number = int(input())

result = smallest_number(first_number, second_number, third_number)

print(result)