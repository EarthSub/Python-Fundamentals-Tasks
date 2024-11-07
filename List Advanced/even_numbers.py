# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.

# Hints
# Read the string, split it, and convert the list of strings into a list of numbers using map function:

#          Example

# Input               Output

# 3, 2, 1, 5, 8       [1, 4]

# 2, 4, 6, 9, 10      [0, 1, 2, 4]



list_as_numbers = list(map(int, input().split(", ")))

even_numbers_index_list = []

for x in range(len(list_as_numbers)):
    if list_as_numbers[x] % 2 == 0:
        even_numbers_index_list.append(x)

print(even_numbers_index_list)