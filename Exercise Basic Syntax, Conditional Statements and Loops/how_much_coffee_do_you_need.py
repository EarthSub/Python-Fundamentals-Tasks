coffee_needed = 0
while True:
    enter_a_command = input()
    if enter_a_command == "END":
         break
    elif enter_a_command == "coding":
        coffee_needed += 1
    elif enter_a_command == "dog" or enter_a_command == "cat":
        coffee_needed += 1
    elif enter_a_command == "movie":
        coffee_needed += 1
    elif enter_a_command == "CODING":
        coffee_needed += 2
    elif enter_a_command == "DOG" or enter_a_command == "CAT":
        coffee_needed += 2
    elif enter_a_command == "MOVIE":
        coffee_needed += 2
if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)
