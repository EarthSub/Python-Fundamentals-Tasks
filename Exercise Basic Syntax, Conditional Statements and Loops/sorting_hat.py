students_names = input()

while students_names != "Welcome!":
    if students_names == "Voldemort":
        print("You must not speak of that name!")
        break
    elif len(students_names) < 5:
        print(f"{students_names} goes to Gryffindor.")
    elif len(students_names) == 5:
        print(f"{students_names} goes to Slytherin.")
    elif len(students_names) == 6:
        print(f"{students_names} goes to Ravenclaw.")
    else:
        print(f"{students_names} goes to Hufflepuff.")
    students_names = input()
if students_names != "Voldemort":
    print("Welcome to Hogwarts.")

