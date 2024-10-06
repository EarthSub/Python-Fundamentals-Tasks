starting_list = input().split(", ")
starting_list = [int(num) for num in starting_list]

for number in starting_list:
    if number == 0:
        starting_list.remove(number)
        starting_list.append(0)

print(starting_list)