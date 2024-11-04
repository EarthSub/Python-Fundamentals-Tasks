# On the first line, you will receive words separated by a single space. On the second line,you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence. Then,
# you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".



# Hints

# First, read all the strings and the searched palindrome, and we create an empty list for the found palindromes:

#                     Example
# Input                                       Output

# wow father mom wow shirt stats
# wow                                         ['wow', 'mom', 'wow', 'stats'] Found palindrome 2 times

# hey how you doin? lol
# mom                                         ['lol'] Found palindrome 0 times


list_of_words = input().split()
special_palindrome = input()

palindromes = []

for word in list_of_words:
    if word == word[::-1]:
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(special_palindrome)} times")
