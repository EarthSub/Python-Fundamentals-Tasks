team_a = [i for i in range(1, 12)]
team_b = [i for i in range(1, 12)]

cards = input()
cards = set(cards.split(" "))

for card in cards:
    if len(team_a) < 7 or len(team_b) < 7:
        break
    if "A" in card:
        team_a.pop()
    elif "B" in card:
        team_b.pop()

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")