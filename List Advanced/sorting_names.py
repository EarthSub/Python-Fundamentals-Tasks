# Write a program that reads a single string with names separated by comma and space ", ".
# Sort the names by their length in descending order. If 2 or more names have the same length,
# sort them in ascending order (alphabetically). Print the resulting list.

#                     Example

# Input                                       Output

# Ali, Marry, Kim, Teddy, Monika, John        ["Monika", "Marry", "Teddy", "John", "Ali", "Kim"]

# Lilly, Tim, Kate, Tom, Alex                 ['Lilly', 'Alex', 'Kate', 'Tim', 'Tom']



names_list = input().split(", ")

sorted_list = sorted(names_list, key=lambda w: (-len(w), w))

print(sorted_list)
