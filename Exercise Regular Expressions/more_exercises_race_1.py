# Write a program that processes information about a race. On the first line,
# you will be given a list of participants separated by ", ".
# On the next few lines until you receive a line "end of race" you will be given
# some info which will be some alphanumeric characters. In between them,
# you could have some extra characters which you should ignore. For example:
# "G!32e%o7r#32g$235@!2e". The letters are the name of the person and the sum of the digits is the distance he ran.
# So here we have George who ran 29 km. Store the information about the person only if
# the list of racers contains the name of the person. If you receive the same person more than
# once just add the distance to his old distance.
# At the end print the top 3 racers ordered by distance in descending in the format:

# "1st place: {first racer}

# 2nd place: {second racer}

# 3rd place: {third racer}"


#                                         Examples

# Input                                   Output                                  Comment

# George, Peter, Bill, Tom                1st place: George                       On the 3rd input line, we have Ray. He
# G4e@55or%6g6!68e!!@                     2nd place: Peter                        is not on the list, so we do not count
# R1@!3a$y4456@                           3rd place: Tom                          his results. The other ones are valid.
# B5@i@#123ll                                                                     George has a total of 55 km, Peter has
# G@e54o$r6ge#                                                                    25 and Tom has 19. We do not print Bill
# 7P%et^#e5346r                                                                   because he is in 4th place.
# T$o553m&6
# end of race


import re

list_of_names = input().split(", ")

race_dict = {}

while True:
    some_info = input()
    if some_info == "end of race":
        break

    name_pattern = r"[A-Za-z]"

    letters = re.findall(name_pattern, some_info)
    name = "".join(letters)

    points_pattern = r"\d"

    digits = re.findall(points_pattern, some_info)
    points = sum(int(digit) for digit in digits)

    if name in list_of_names:
        if name in race_dict:
            race_dict[name] += points
        else:
            race_dict[name] = points


sorted_items = sorted(race_dict.items(), key=lambda item: item[1], reverse=True)

for i, (name, distance) in enumerate(sorted_items[:3], start=1):
        suffix = ""
        if i == 1: suffix = "st"
        elif i == 2: suffix = "nd"
        elif i == 3: suffix = "rd"
        print(f"{i}{suffix} place: {name}")