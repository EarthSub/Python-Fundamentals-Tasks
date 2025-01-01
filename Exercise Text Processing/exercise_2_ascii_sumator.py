# Write a program that prints the sum of all found characters between two given characters (their ASCII code).
# On each of the first two lines, you will receive a single character. On the last line, you get a random string.
# Print the sum of the ASCII values of all characters in the random string between the two given characters in the ASCII table.


#                             Example

# Input                       Output                      Comment
#
# .                           363                         The found characters are 1, 2, 5, 6, 5, 3 and 5. Their
# @                                                       ASCII sum is 49 + 50 + 53 + 54 + 53 + 51 + 53 = 363.
# dsg12gr5653feee5

# ?                           262
# E
# @ABCEF


starting_point = input()
ending_point = input()
string_to_iterate = input()
total_sum = 0

for char in string_to_iterate:
    if ord(starting_point) < ord(char) < ord(ending_point):
        total_sum += ord(char)

print(total_sum)