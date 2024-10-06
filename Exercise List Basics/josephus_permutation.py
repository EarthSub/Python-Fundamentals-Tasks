starting_list = input().split()
step = int(input())

exiting_list = []
index_to_pop = 0
while len(starting_list) > 0:
    index_to_pop = (index_to_pop + step - 1) % len(starting_list)
    exiting_list.append(starting_list.pop(index_to_pop))

print(f"[{','.join(exiting_list)}]")