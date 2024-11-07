# You will receive two lines of input:
# · a list of employees' happiness as a string of numbers separated by a single space
# · a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# · If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# · Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

#                                     Example

# Input                   Output                                      Comment

# 1 2 3 4 2 1
# 3                       Score: 2/6. Employees are not happy!        After the mapping:
#                                                                     3 6 9 12 6 3
#                                                                     After the filtration:
#                                                                     9 12
#                                                                     2/6 people are happy, so the overall
#                                                                     happiness is bad

# 2 3 2 1 3 3
# 4                       Score: 3/6. Employees are happy!            Half of the people are happy, so the overall
#                                                                     happiness is good





employees_happiness = list(map(int, input().split()))
factor = int(input())

multiplied_happiness = [num * 3 for num in employees_happiness]
average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
multiplied_happiness = [num for num in multiplied_happiness if num >= average_happiness]

if len(multiplied_happiness) >= (len(employees_happiness) / 2):
    print(f"Score: {len(multiplied_happiness)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(multiplied_happiness)}/{len(employees_happiness)}. Employees are not happy!")