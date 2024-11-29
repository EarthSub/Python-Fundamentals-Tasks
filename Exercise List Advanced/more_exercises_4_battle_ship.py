# You will be given a number n representing the number of rows of the field. On the following n lines,
# you will receive each field row as a string with numbers separated by a space.
# Each number greater than zero represents a ship with health equal to the number value.
#
# After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}".
# Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1.
# If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed.


# Example

# Input                               Output                  Comment

# 3                                   2                       States after each attack:
# 1 0 0 1                                                     First attack -> 1 ship destroyed
# 2 0 0 0                                                     0 0 0 1
# 0 3 0 1                                                     2 0 0 0
# 0-0 1-0 2-1 2-1 2-1 1-1 2-1                                 0 3 0 1
#                                                             Second attack -> reduce ship health
#                                                             0 0 0 1
#                                                             1 0 0 0
#                                                             0 2 0 1
#                                                             Third attack -> reduce ship health
#                                                             0 0 0 1
#                                                             2 0 0 0
#                                                             0 2 0 1
#                                                             Fourth attack -> reduce ship health
#                                                             0 0 0 1
#                                                             2 0 0 0
#                                                             0 1 0 1
#                                                             Fifth attack -> another ship destroyed
#                                                             0 0 0 1
#                                                             2 0 0 0
#                                                             0 0 0 1
#                                                             Sixth and Seventh attack -> no ship destroyed


# 5                                   2
# 1 0 5 0 1
# 6 3 9 0 0
# 7 9 4 3 2
# 1 0 0 4 9
# 5 6 0 3 5
# 0-1 0-2 0-2 0-2 0-2 0-2 3-0


def attack(ships: list):
    sunken_ship = 0
    commands_to_attack = input().split()
    for attempt in range(len(commands_to_attack)):
        string = commands_to_attack[attempt]
        current_attack = [n for n in string if n.isdigit()]
        rows = int(current_attack[0])
        columns = int(current_attack[1])
        if 0 <= rows < len(ships) and 0 <= columns < len(ships[0]):
            if ships[rows][columns] > 0:
                ships[rows][columns] -= 1
                if ships[rows][columns] == 0:
                    sunken_ship += 1
    return sunken_ship




rows_of_the_field = int(input())
ship_placement = []

for row in range(rows_of_the_field):
    ship_placement.append(list(map(int, input().split())))


sunken = attack(ship_placement)
print(sunken)