# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:

# · "Shadowmourne" - requires 250 Shards
# · "Valanyr" - requires 250 Fragments
# · "Dragonwrath" - requires 250 Motes

# "Shards", "Fragments", and "Motes" are the key materials (case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race.
# At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, and motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.

# Input
# · Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"

# Output
# · On the first line, print the obtained item in the format: "{Legendary item} obtained!"
# · On the next three lines, print the remaining key materials
# · On the several final lines, print the junk items
# · All materials should be printed in the format: "{material}: {quantity}"
# · The output should be lowercase, except for the first letter of the legendary


#                         Examples

# Input                                               Output

# 3 Motes 5 stones 5 Shards                           Valanyr obtained!
# 6 leathers 255 fragments 7 Shards                   shards: 5
#                                                     fragments: 5
#                                                     motes: 3
#                                                     stones: 5
#                                                     leathers: 6

# 123 silver 6 shards 8 shards 5 motes                Dragonwrath obtained!
# 9 fangs 75 motes 103 MOTES 8 Shards                 shards: 22
# 86 Motes 7 stones 19 silver                         fragments: 0
#                                                     motes: 19
#                                                     silver: 123
#                                                     fangs: 9


materials = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False

while not obtained:
    current_material = input().split()
    for item in range(0, len(current_material), 2):
        recourse = current_material[item + 1].lower()
        quantity = int(current_material[item])
        if recourse not in materials.keys():
            materials[recourse] = 0
        materials[recourse] += quantity
        if materials["shards"] >= 250:
            print("Shadowmourne obtained!")
            materials["shards"] -= 250
            obtained = True
        elif materials["fragments"] >= 250:
            print("Valanyr obtained!")
            materials["fragments"] -=250
            obtained = True
        elif materials["motes"] >= 250:
            print("Dragonwrath obtained!")
            materials["motes"] -= 250
            obtained = True
        if obtained:
            break

for recourse, quantity in materials.items():
    print(f"{recourse}: {quantity}")