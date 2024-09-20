while True:
    enter_string = input()
    if enter_string == "End":
        break
    if enter_string == "SoftUni":
        continue
    for character in enter_string:
        phrase = character * 2
        print(phrase, end="")
    print()