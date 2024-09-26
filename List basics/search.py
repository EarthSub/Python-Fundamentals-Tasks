numbers_of_lines = int(input())
special_word = input()

list_with_words = []
phrase_with_special_word = []
for _ in range(numbers_of_lines):
    current_word = input()
    list_with_words.append(current_word)
    if special_word in current_word:
        phrase_with_special_word.append(current_word)

print(list_with_words)
print(phrase_with_special_word)