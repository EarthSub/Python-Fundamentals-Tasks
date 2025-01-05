# Write a program that finds how many times a word is used in a string.
# The output is a single number indicating the number of times the string contains the word.
# Note that letter case does not matter – it is case-insensitive.


#                                         Examples

# Input                                                                               Output

# The waterfall was so high, that the child couldn't see its peak.                    2
# the

# How do you plan on achieving that? How? How can you even think of that?             3
# how

# There was one. Therefore I bought it. I wouldn't buy it otherwise.                  1
# there


import re

sentence = input()
searching_word = input()


pattern = fr"(?i)\b{searching_word}\b"
result = re.findall(pattern, sentence)

print(len(result))