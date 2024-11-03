# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".

# Return a list containing all to-do notes sorted by importance in ascending order.

# The importance value will always be an integer between 1 and 10 (inclusive).

# Hint
# · Use the pop() and insert() methods.

#             Example

# Input                   Output

# 2-Walk the dog
# 1-Drink coffee
# 6-Dinner                ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']
# 5-Work
# End

# 3-C
# 2-A
# 1-B                     ['B', 'A', 'C', 'V']
# 6-V
# End


notes = ["0"] * 10

while True:
    command = input()
    if command == "End":
        break
    split_command = command.split("-")
    priority = int(split_command[0]) - 1
    note = split_command[1]
    notes.pop(priority)
    notes.insert(priority, note)

final_notes = [word for word in notes if word != "0"]
print(final_notes)
