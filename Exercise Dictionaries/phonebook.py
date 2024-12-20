# Write a program that receives info from the console about people and their phone numbers.

# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.

# After filling out the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and
# print its details in the format: "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."

#               Examples

# Input                           Output

# Adam-0888080808                 Contact Mery does not exist.
# 2                               Adam -> 0888080808
# Mery
# Adam

# Adam-+359888001122              Silvester -> 02/987665544
# Ralf-666                        Contact silvester does not exist.
# George-5559393                  Contact Rolf does not exist.
# Silvester-02/987665544          Ralf -> 666
# 4
# Silvester
# silvester
# Rolf
# Ralf


phone_book = {}
searching_times = 0

while True:
    address = input()
    if address.isdigit():
        searching_times = int(address)
        break
    contact = address.split("-")
    name = contact[0]
    phone = contact[1]
    if name not in phone_book:
        phone_book[name] = phone
    else:
        phone_book[name] = phone

for _ in range(searching_times):
    current_name = input()
    if current_name in phone_book:
        print(f"{current_name} -> {phone_book[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")

