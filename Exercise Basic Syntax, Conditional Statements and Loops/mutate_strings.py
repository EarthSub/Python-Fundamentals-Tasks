first_string = input()
second_string = input()
latest_printed_phase = first_string
for character in range(len(first_string)):
    first_part = second_string[:character + 1]
    second_part = first_string[character + 1:]
    phrase = first_part + second_part
    if phrase != latest_printed_phase:
        print(phrase)
        latest_printed_phase = phrase
