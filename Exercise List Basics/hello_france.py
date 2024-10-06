item_list = input().split("|")
budget = float(input())
ticket_price = 150
money_spent = 0
money_earned = 0
list_with_sold_items = []

for x in range(len(item_list)):
    trade = item_list[x].split("->")
    item = trade[0]
    price = float(trade[1])
    if price > budget:
        continue
    if (item == "Clothes") and (price <= 50) \
            or (item == "Shoes") and (price <= 35) \
            or (item == "Accessories") and (price <= 20.50):
        money_spent += price
        budget -= price
        sold_item = price * 1.4
        money_earned += sold_item
        list_with_sold_items.append(f"{sold_item:.2f}")

print(" ".join(map(str, list_with_sold_items)))
profit = money_earned - money_spent
print(f"Profit: {profit:.2f}")
budget += money_earned
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")