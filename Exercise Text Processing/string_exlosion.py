# Write a program that reads a string from the console that contains:

# · Explosions marked with '>'
# · Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# · Any other characters

# Your task is to delete x characters, starting after the exploded character ('>').
# If you find another explosion mark ('>') while deleting characters,
# you should add the strength to your previous explosion. You should not delete the explosion character – '>'.

# When all characters are processed, print the final string.

# Constraints

# · You will always receive strength for the explosions
# · The path will consist only of letters from the Latin alphabet, integers, and the char '>'
# · The strength of the punches will be in the interval [0…9]


#                                             Examples

# Input                                       Output                          Comments

# abv>1>1>2>2asdasd                           abv>>>>dasd                     1st explosion is at index 3, with a
#                                                                             strength of 1.We delete only the
#                                                                             digit after the explosion character.
#                                                                             The string will look like this:
#                                                                             abv>>1>2>2asdasd
#                                                                             2nd explosion is with strength one,
#                                                                             and the string transforms to this:
#                                                                             abv>>>2>2asdasd
#                                                                             3rd explosion is now with a strength
#                                                                             of 2. We delete the digit, and we
#                                                                             find another explosion. At this
#                                                                             point, the string looks like this:
#                                                                             abv>>>>2asdasd.
#                                                                             4th explosion is with strength 2. We
#                                                                             have 1 strength left from the
#                                                                             previous explosion, and we add the
#                                                                             strength of the current explosion to
#                                                                             what is left, which adds up to a total
#                                                                             strength of 3. We delete the next
#                                                                             three characters, and we receive
#                                                                             the string abv>>>>dasd
#                                                                             We do not have any more
#                                                                             explosions, and we print the result:
#                                                                             abv>>>>dasd

# pesho>2sis>1a>2akarate>4hexmaster           pesho>is>a>karate>master


starting_string = input()
ending_string = ""
explosion_counter = 0

for char in range(len(starting_string)):
    if explosion_counter > 0 and starting_string[char] != ">":
        explosion_counter -= 1
    elif starting_string[char] == ">":
        ending_string += starting_string[char]
        explosion_counter += int(starting_string[char+1])
    else:
        ending_string += starting_string[char]

print(ending_string)
