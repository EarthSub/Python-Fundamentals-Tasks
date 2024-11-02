# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
# Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

#          Examples
#
# Input               Output
#
# Python              Pythn
#
# ILovePython         LvPythn



word = input()
new_word = [letter for letter in word if letter not in 'a' 'u' 'e' 'i' 'o' 'A' 'U' 'E' 'I' 'O']
print("".join(new_word))