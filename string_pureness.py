number_of_strings = int(input())

for _ in range(number_of_strings):
    enter_a_phrase = input()
    if "," in enter_a_phrase or "." in enter_a_phrase or "_" in enter_a_phrase:
        print(f"{enter_a_phrase} is not pure!")
    else:
        print(f"{enter_a_phrase} is pure.")
