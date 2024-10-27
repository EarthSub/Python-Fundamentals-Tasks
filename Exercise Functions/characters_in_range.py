# Write a function that receives two characters and returns a single string
# with all the characters in between them (according to the ASCII code),
# separated by a single space. Print the result on the console.

#             Examples
#
# Input                           Output
#
#   a                               bc
#   d
#
#   :                               $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9
#   #
#
#   C                               $ % &' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
#   #
#


def char_in_range(first_char: str, second_char: str) -> None:
    for character in range(ord(first_character) + 1, ord(second_character)):
        list_of_characters.append(chr(character))


first_character = input()
second_character = input()
list_of_characters = []

char_in_range(first_character, second_character)
print(" ".join(list_of_characters))
