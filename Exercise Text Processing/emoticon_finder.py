# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.


#                                 Example

# Input                                                           Output

# There are so many emoticons nowadays :P. I have many            :P
# ideas :O what input to place here :)                            :O
#                                                                 :)


text = input()
for word in range(len(text)):
    if text[word] == ":":
        print(f":{text[word+1]}")
