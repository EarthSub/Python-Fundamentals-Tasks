# You are a facility manager at a large business center.
# One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.

# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors.
# Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end.
# For example: "XXXXX 4" (5 chairs and 4 visitors).

# Keep track of the free chairs:
# · If there are not enough chairs in a specific room, print the following message:
# "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
# · Otherwise, print: "Game On, {total_free_chairs} free chairs left".

#             Example

# Input                       Output

# 4
# XXXX 4
# XX 1                        Game On, 4 free chairs left
# XXXXXX 3
# XXX 3


# 3
# XXXXXXX 5                   1 more chairs needed in room 2
# XXXX 5                      2 more chairs needed in room 3
# XXXXXX 8


number_of_rooms = int(input())
chairs_left = 0
chairs_in_need = 0
for rooms in range(1, number_of_rooms + 1):
    info_list = input().split()
    chairs = info_list[0]
    people = int(info_list[1])
    if len(chairs) < people:
        chairs_in_need += people - len(chairs)
        print(f"{people - len(chairs)} more chairs needed in room {rooms}")
    else:
        chairs_left += len(chairs) - people
free_chairs = chairs_left - chairs_in_need
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
