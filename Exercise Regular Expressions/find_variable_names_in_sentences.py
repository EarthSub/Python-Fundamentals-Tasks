# Write a program that finds all variable names in each string. A variable name starts with an underscore ("_") and
# contains only capital and non-capital letters and digits. Extract only their names without the underscore.
# Try to do this only with regular expressions.

# The output consists of all variable names extracted and printed on a single line, separated by a comma.


#                                     Examples

# Input                                                                   Output

# The _id and _age variables are both integers.                           id,age

# Calculate the _area of the _perfectRectangle object.                    area,perfectRectangle

# __invalidVariable _evenMoreInvalidVariable_ _validVariable              validVariable


import re

sentences = input()

pattern = r"\b_([A-Za-z0-9]+)\b"
result = re.findall(pattern, sentences)
print(",".join(result))
