# Create a class Party that only has an attribute people – empty list. The __init__ method should not accept any parameters.
# You will be given names of people (on separate lines) until you receive the command "End".
# Use the created class to solve this problem. After you receive the "End" command, print 2 lines:

# · "Going: {people}" - the people should be separated by comma and space ", ".

# · "Total: {total_people_going}"

# Note: submit all of your code, including the class


#         Example

# Input               Output

# Peter               Going: Peter, John, Katy
# John                Total: 3
# Katy
# End

# Sam                 Going: Sam, Eddy, Edd, Kris
# Eddy                Total: 4
# Edd
# Kris
# End





class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    name = input()
    if name == "End":
        break
    party.people.append(name)


print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")