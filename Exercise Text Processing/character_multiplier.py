# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with
# str2[0] and add the result to the total sum, then continue with the next two characters.
# If one of the strings is longer than the other, add the remaining character codes to
# the total sum without multiplication.


#             Examples

# Input                       Output

# George Peter                52114

# 123 522                     7647

# a aaaa                      9700


first_string, second_string = input().split()
total_sum = 0

min_len = min(len(first_string), len(second_string))

for letter in range(min_len):
    total_sum += ord(first_string[letter]) * ord(second_string[letter])

if len(first_string) > len(second_string):
    for letter in range(min_len, len(first_string)):
        total_sum += ord(first_string[letter])

else:
    for letter in range(min_len, len(second_string)):
        total_sum += ord(second_string[letter])

print(total_sum)

