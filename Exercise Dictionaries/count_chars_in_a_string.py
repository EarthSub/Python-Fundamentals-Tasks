# Write a program that counts all characters in a string except for space (" ").

# Print all the occurrences in the following format:

# "{char} -> {occurrences}"


#         Examples

# Input               Output

# text                t -> 2
#                     e -> 1
#                     x -> 1

# text text text      t -> 6
#                     e -> 3
#                     x -> 3



some_text = input()

repeating_char = {}

for char in some_text:
    if char != " ":
        if char not in repeating_char:
            repeating_char[char] = 0
        repeating_char[char] += 1

for character in repeating_char:
    print(f"{character} -> {repeating_char[character]}")
