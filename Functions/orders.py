# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water",
# or "snacks", and a quantity of the product. The prices for a single piece of each product are:
#
# · coffee - 1.50
#
# · water - 1.00
#
# · coke - 1.40
#
# · snacks - 2.00
#
# Print the result formatted to the second decimal place.


def total_price(product: str, quantity: int) -> float:
    if product == "coffee":
        return quantity * 1.50
    elif product == "water":
        return quantity * 1.00
    elif product == "coke":
        return quantity * 1.40
    elif product == "snacks":
        return quantity * 2.00


prod = input()
quant = int(input())

result = total_price(prod, quant)
print(f"{result:.2f}")