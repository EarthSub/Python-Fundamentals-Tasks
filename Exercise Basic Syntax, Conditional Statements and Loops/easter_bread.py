budget = float(input())
price_for_1kg_flour = float(input())

price_for_1pack_eggs = price_for_1kg_flour * 0.75
price_for_1liter_milk = price_for_1kg_flour + (price_for_1kg_flour * 0.25)
price_for_one_loaves = price_for_1kg_flour + price_for_1pack_eggs + (price_for_1liter_milk * 0.25)

loaves_made = 0
eggs_earned = 0

while budget > price_for_one_loaves:
    loaves_made += 1
    budget -= price_for_one_loaves
    eggs_earned += 3
    if loaves_made % 3 == 0:
        lost_eggs = loaves_made - 2
        eggs_earned -= lost_eggs

print(f'You made {loaves_made} loaves of Easter bread! Now you have {eggs_earned} eggs and {budget:.2f}BGN left.')