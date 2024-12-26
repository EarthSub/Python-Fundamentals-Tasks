# Write a program that receives a text and a string of banned words, separated by a comma and space ", ".
# All banned words in the text should be replaced with the number of asterisks "*", equal to the word's length.

# The ban list will be entered on the first input line and the text - on the second input line.


#                             Examples

# Input                                                       Output

# Linux, Windows                                              It is not *****, it is GNU/*****. *****
# It is not Linux, it is GNU/Linux. Linux is                  is merely the kernel, while GNU adds the
# merely the kernel, while GNU adds the                       functionality. Therefore we owe it to them
# functionality. Therefore we owe it to them                  by calling the OS GNU/*****! Sincerely, a
# by calling the OS GNU/Linux! Sincerely, a                   ******* client
# Windows client




banned_words = input().split(", ")
text = input()

for word in banned_words:
    while word in text:
        text = text.replace(word, "*" * len(word))

print(text)