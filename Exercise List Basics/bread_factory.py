working_event = input().split("|")
energy = 100
coins = 100
handle_all_events = True

for order in range(len(working_event)):
    event_list = working_event[order].split("-")
    event = event_list[0]
    quantity = int(event_list[1])
    if event == "rest":
        current_energy = energy
        energy += quantity
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
        else:
            energy -= 30
            coins += quantity
            print(f"You earned {quantity} coins.")
    else:
        if coins >= quantity:
            coins -= quantity
            print(f"You bought {event}.")
        else:
            handle_all_events = False
            print(f"Closed! Cannot afford {event}.")
            break

if handle_all_events:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")