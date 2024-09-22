import random

computer_random_number = random.randint(1, 100)


while True:
    player_input = input("Guess the number (1-100): ")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_input = int(player_input)

    if player_input == computer_random_number:
        print("You guessed it!")
        break
    elif player_input > computer_random_number:
        print("Too High!")
    else:
        print("Too Low!")
