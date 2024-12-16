# You will receive a single line containing some food (keys) and quantities (values).
# They will be separated by a single space (the first element is the key, the second – is the value, and so on).
# Create a dictionary with all the keys and values and print it on the console.

#                     Example

# Input                                        Output

# bread 10 butter 4 sugar 9 jam 12            {'bread': 10, 'butter': 4, 'sugar': 9, 'jam': 12}
# eggs 3 sugar 7 salt 1 butter 3              {'eggs': 3, 'sugar': 7, 'salt': 1, 'butter': 3}


list_with_foods = input().split()

dict_with_foods = {}

for food in range(0, len(list_with_foods), 2):
    foods = list_with_foods[food]
    quantity = list_with_foods[food + 1]
    dict_with_foods[foods] = int(quantity)

print(dict_with_foods)