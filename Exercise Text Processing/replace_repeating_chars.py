# Write a program that reads a string from the console and replaces any
# sequence of the same letters with a single corresponding letter.


#                     Examples

# Input                                       Output

# aaaaabbbbbcdddeeeedssaa                     abcdedsa

# qqqwerqwecccwd                              qwerqwecwd


text = input()
new_text = ""

for index in range(len(text)):
    if not new_text or text[index] != new_text[-1]:
        new_text += text[index]

print(new_text)