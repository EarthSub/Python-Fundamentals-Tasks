number_of_interactions = int(input())

phrase = ""

for _ in range(number_of_interactions):
    number = int(input())
    if number == 88:
        phrase = "Hello"
    elif number == 86:
        phrase = "How are you?"
    elif number < 88:
        phrase = "GREAT!"
    elif number > 88:
        phrase = "Bye."
    print(phrase)