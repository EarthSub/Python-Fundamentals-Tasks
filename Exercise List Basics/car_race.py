starting_list = input().split()
list_divider = len(starting_list) // 2

left_car_time = starting_list[:list_divider]
right_car_time = starting_list[list_divider + 1:]

current_left_car_time = 0
current_right_car_time = 0

for num in left_car_time:
    if int(num) == 0:
        current_left_car_time *= 0.8
    else:
        current_left_car_time += int(num)

for num in range(len(starting_list) - 1, list_divider, -1):
    if int(starting_list[num]) == 0:
        current_right_car_time *= 0.8
    else:
        current_right_car_time += int(starting_list[num])

if current_right_car_time < current_left_car_time:
    print(f"The winner is right with total time: {current_right_car_time:.1f}")
else:
    print(f"The winner is left with total time: {current_left_car_time:.1f}")