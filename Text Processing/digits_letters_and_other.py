# Write a program that receives a single string. On the first line, print all the digits found in the string,
# on the second – all the letters, and on the third – all the other characters.
# There will always be at least one digit, one letter, and one other character.


#                 Examples

# Input                               Output

# Agd#53Dfg^&4F53                     53453
#                                     AgdDfgF
#                                     #^&


text = input()

digits = ""
letters = ""
others = ""

for char in text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    elif char.isascii():
        others += char

print(digits)
print(letters)
print(others)