# You will be given strings on separate lines until you receive an "end" command.
# Write a program that reverses strings and prints each pair on a separate line in the format "{word} = {reversed_word}".


#         Examples

# Input               Output

# helLo               helLo = oLleh
# Softuni             Softuni = inutfoS
# bottle              bottle = elttob
# end

# Dog                 Dog = goD
# caT`                caT = Tac
# chAir               chAir = riAhc
# end


while True:
    text = input()
    if text == "end":
        break
    reversed_text = text[::-1]
    print(f"{text} = {reversed_text}")