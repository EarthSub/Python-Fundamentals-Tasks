# Write a program that receives a sequence of numbers,
# separated by a single space,
# and prints their absolute value as a list.
# Use abs().


list_of_numbers = list(map(float, input().split()))
absolute_values = []

for num in list_of_numbers:
    absolute_values.append(abs(num))

print(absolute_values)