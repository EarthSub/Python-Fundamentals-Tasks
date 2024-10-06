cards = input().split()
count_of_shuffle = int(input())

for shuffle in range(count_of_shuffle):
    half = len(cards) // 2
    left_half = cards[:half]
    right_half = cards[half:]
    shuffled_deck = []
    for card_index in range(half):
        shuffled_deck.append(left_half[card_index])
        shuffled_deck.append(right_half[card_index])
    cards = shuffled_deck

print(cards)