# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:

# · If the product doesn't exist yet, add it with its starting quantity.
# · If you receive a product, that already exists, increase its quantity by the input quantity
# and if its price is different, replace the price as well.

# You will receive products(' names, prices, and quantities on new lines.' Until you receive the command "buy",
# keep adding items. Finally, print all items with their names and the total price of each product.)

# Input
# · Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# · The product data is always delimited by a single space.

# Output
# · Print information about each product in the following format: "{product_name} -> {total_price}"
# · Format the total price to the 2nd digit after the decimal separator.


#                  Examples

# Input                               Output

# Beer 2.20 100                       Beer -> 220.00
# IceTea 1.50 50                      IceTea -> 75.00
# NukaCola 3.30 80                    NukaCola -> 264.00
# Water 1.00 500                      Water -> 500.00
# buy

# Beer 2.40 350                       Beer -> 660.00
# Water 1.25 200                      Water -> 250.00
# IceTea 5.20 100                     IceTea -> 110.00
# Beer 1.20 200
# IceTea 0.50 120
# buy

# CesarSalad 10.20 25                 CesarSalad -> 255.00
# SuperEnergy 0.80 400                SuperEnergy -> 320.00
# Beer 1.35 350                       Beer -> 472.50
# IceCream 1.50 25                    IceCream -> 37.50
# buy



dict_of_products = {}
ls = {}
while True:
    the_input = input()
    if the_input == "buy":
        break
    name, price, quantity = the_input.split()
    if name not in dict_of_products:
        dict_of_products[name] = 0
    dict_of_products[name] += float(quantity)
    ls[name] = float(price)
    if name in ls:
        if ls[name] != float(price):
            ls[name] = float(price)

new_dict = {key: dict_of_products[key] * ls[key] for key in dict_of_products if key in ls}

for product in new_dict:
    print(f"{product} -> {new_dict[product]:.2f}")
