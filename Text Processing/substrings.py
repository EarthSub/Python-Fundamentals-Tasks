# On the first line, you will receive a string. On the second line, you will receive a second string.
# Write a program that removes all the occurrences of the first string in the second until there is no match.
# At the end, print the remaining string.


#                     Examples

# Input               Output              Comment

# ice                 kgb                 We remove ice once and we get "kgiciceeb"
# kicegiciceeb                            We match "ice" one more time and we get "kgiceb"
#                                         There is one more match. The finam result is "kgb"


first_string = input()
second_string = input()

while first_string in second_string:
    second_string = second_string.replace(first_string, "")

print(second_string)