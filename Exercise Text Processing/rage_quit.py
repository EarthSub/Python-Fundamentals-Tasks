# Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team;
# he wants something truly spectacular. He asks for your help.

# He('ll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N), e.g.'
#    ', "a3". You need to convert the letters to uppercase for each string and print it repeatedly N times on the console.'
#    ' In the example, you need to write back "AAA".)

# First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive)
# in the format: "Unique symbols used {0}".

# Next, print the rage message itself.

# The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol,
# and for each string, there will be a corresponding number. The input will be given on a single line.

# Input

# · The input data should be read from the console.
# · It consists of a single line holding a series of string-number sequences.
# · The input data will always be valid. There is no need to check it explicitly.

# Output

# · The output should be printed on the console. It should consist of exactly two lines:
#     o On the first line, print the number of unique symbols used in the message in the format described above.
#     o On the second line, print the rage message.

# Constraints

# · The count of string-number pairs will be in the range [1 … 20 000].
# · Each string will contain any character except digits. The length of each string will be in the range [1 … 20].
# · The repeat count for each string will be an integer in the range [0 … 20].
# · Allowed working time for your program: 0.3 seconds. Allowed memory: 64 MB.


#                         Examples

# Input                   Output                          Comments

# a3                      Unique symbols used: 1          We have just one string-number pair. The symbol is 'a', convert it
#                         AAA                             to uppercase and repeat 3 times: AAA.
#                                                         Only one symbol is used ('A').

# aSd2&5s@1               Unique symbols used: 5          ASDASD&&&&&S@ "aSd" is converted to "ASD" and repeated twice; "&" is repeated 5
#                         ASDASD&&&&&S@                   times; "s@" is converted to "S@" and repeated once.
#                                                         5 symbols are used: 'A', 'S', 'D', '&' and '@'.



initial_string = input()
finale_string = ""
current_string = ""
multiplier = ""

for char in range(len(initial_string)):
    if not initial_string[char].isdigit():
        current_string += initial_string[char].upper()
    else:
        for next_char in range(char, len(initial_string)):
            if not initial_string[next_char].isdigit():
                break
            multiplier += initial_string[next_char]
        finale_string += current_string * int(multiplier)
        current_string = ""
        multiplier = ""

print(f"Unique symbols used: {len(set(finale_string))}")
print(finale_string)