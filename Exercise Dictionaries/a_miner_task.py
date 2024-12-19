# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.

# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"

# The quantities will be in the range [1 … 2 000 000 000].


#         Examples

# Input               Output

# Gold                Gold -> 155
# 155                 Silver -> 10
# Silver              Copper -> 17
# 10
# Copper
# 17
# stop

# gold                gold -> 170
# 155                 silver -> 10
# silver              copper -> 17
# 10
# copper
# 17
# gold
# 15
# stop



miner_stash = {}

while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())
    if command not in miner_stash:
        miner_stash[command] = 0
    miner_stash[command] += quantity


for word in miner_stash:
    print(f"{word} -> {miner_stash[word]}")
