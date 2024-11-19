# You are given a secret message you should decipher. To do that, you need to know that in each word:

# · the second and the last letter are switched (e.g., Holle means Hello)
# · the first letter is replaced by its character code (e.g., 72 means H)

#                 Example

# Input                           Output

# 72olle 103doo 100ya             Hello good day

# 82yade 115te 103o               Ready set go



secret_message = input().split()

deciphered_list = []

for word in secret_message:
    ascii_tab = []
    current_word = []
    for character in word:
        if character.isdigit():
            ascii_tab.append(character)
        else:
            current_word.append(character)
    ascii_tab = "".join(ascii_tab)
    first_char = chr(int(ascii_tab))
    current_word[0], current_word[-1] = current_word[-1], current_word[0]
    current_word = "".join(current_word)
    deciphered_list.append(first_char + current_word)

print(" ".join(deciphered_list))