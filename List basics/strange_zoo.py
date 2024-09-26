back_to_normal = []

for roll in range(3):
    current_part = input()
    back_to_normal.append(current_part)

back_to_normal[0], back_to_normal[2] = back_to_normal[2], back_to_normal[0]
print(back_to_normal)
