gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    commands_list = command.split()

    if "OutOfStock" in commands_list:
        gift_to_remove = commands_list[1]
        for x in range(len(gifts)):
            if gifts[x] == gift_to_remove:
                gifts[x] = "None"
    elif "Required" in commands_list:
        gift_to_replace = commands_list[1]
        index = int(commands_list[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift_to_replace
    elif "JustInCase" in commands_list:
        gift_to_insert = commands_list[1]
        gifts[-1] = gift_to_insert

print(" ".join(x for x in gifts if x != "None"))