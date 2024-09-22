# Prompt the user to choose a data type to perform operations on
print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

choice = input("Enter the number of your choice (1-4): ")
print()

if choice == '1':
    print("You Chose Strings")
    print()
    print("We have this string \"Learning Python is fun!\"")
    sentence = "Learning Python is fun!"
    print("Extract only one word form the string.")
    print(sentence[8 : 15])
    print("Phrase in upper case.")
    print(sentence.upper())
    new_sentence = sentence.replace("fun", "awesome")
    print("Changing word with other.")
    print(new_sentence)

elif choice == '2':
    print("You Chose Numbers")
    print()
    first_number = float(input("Please enter first number: "))
    second_number = float(input("Please enter second number: "))
    if second_number == 0:
        print("Cannot be divided by zero! Try again.")
    else:
        print(f"Addition: {first_number + second_number}")
        print(f"Subtraction: {first_number - second_number}")
        print(f"Multiplication: {first_number * second_number}")
        print(f"Division: {first_number / second_number}")
        print(f"{first_number} raised to the power of {second_number} is: {first_number ** second_number}")

elif choice == '3':
    print("You Chose Booleans")
    print()
    is_python_fun = True
    is_sunny = False
    print("True and False gives us:", is_python_fun and is_sunny)
    print("True or False gives us:", is_python_fun or is_sunny)
    print("not True or not False gives us:", not is_python_fun, not is_sunny)
    print()
    print("Comparison operations:")
    print("10 > 5", 10 > 5)
    print("5 < 10", 5 < 10)
    print("5 = 5", 5 == 5)
    print()
    print("10 < 5", 10 < 5)
    print("5 > 10", 5 > 10)
    print("10 = 5", 103 == 5)

elif choice == '4':
    print("4. Additional Data Types (List, Tuple, Dictionary)")
    print("4.1 - \"lists\"")
    print()
    print("Printing a list with mixed data types [3, 6, 9, \"three\", \"six\", \"nine\", 3 < 6 < 9]")
    current_list = [3, 6, 9, "three", "six", "nine", 3 < 6 < 9]
    print()
    print("Append a new element to the list and print the updated list.")
    current_list.append("PYTHON IS GREAT!")
    print(current_list)
    print()
    print("Printing forth element form list.")
    print(current_list[4])
    print()
    print("4.2 - \"tuple\"")
    print()
    print("Creating a tuple(3, 6, 9, \"three\", \"six\", \"nine\", 3 < 6 < 9)")
    current_tuple = (3, 6, 9, "three", "six", "nine", 3 < 6 < 9)
    print()
    print("Printing the length of the tuple.")
    print(len(current_tuple))
    print()
    print("Trying to modify one element in the tuple and handle the resulting TypeError.")
    print("current_tuple[0] = 1")
    try:
        current_tuple[0] = 1
    except TypeError as e:
        print("Tuples are immutable, so you cannot change them.")
        print(f"Error: {e}")
    print()
    print("4.3 - \"dictionary\"")
    print()
    print("Create a dictionary with some key-value pairs (e.g., name, age, city)")
    info_dict = {"name": "Jack", "age": 33, "city": "Bogota"}
    print(info_dict)
    print()
    print("Accessing and printing the value for one of the keys (e.g., \"age\").")
    print(info_dict["age"])
    print()
    print("Adding a new key-value pair to the dictionary and print the updated dictionary.")
    info_dict["gender"] = "male"
    print(info_dict)

else:
    print("Unknown operation! Please Choose operation between: 1 - 4")