fire_cells = input().split("#")
amount_of_water = int(input())
effort = 0
total_fire = 0
print("Cells:")
for x in range(len(fire_cells)):
    fire_cell = fire_cells[x].split()
    if fire_cell[0] == "High" and 80 < int(fire_cell[2]) <= 125 and amount_of_water >= int(fire_cell[2]) \
            or fire_cell[0] == "Medium" and 50 < int(fire_cell[2]) <= 80 and amount_of_water >= int(fire_cell[2]) \
            or fire_cell[0] == "Low" and 1 <= int(fire_cell[2]) <= 50 and amount_of_water >= int(fire_cell[2]):
        amount_of_water -= int(fire_cell[2])
        total_fire += int(fire_cell[2])
        effort_percentage = fire_cell[2]
        effort += int(effort_percentage) * 0.25
        print(f"- {fire_cell[2]}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire:}")