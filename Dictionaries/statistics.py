# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
# Sometimes you may receive a product more than once. In that case, you have to add the new quantity to the existing one.
# When you receive the "statistics" command, print the following:

# "Products in stock:

# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"


#                 Example

# Input                           Output

# bread: 4                        Products in stock:
# cheese: 2                       - bread: 5
# ham: 1                          - cheese: 2
# bread: 1                        - ham: 1
# statistics                      Total Products: 3
#                                 Total Quantity: 8


# eggs: 10                        Products in stock:
# bread: 6                        - eggs: 10
# cheese: 8                       - bread: 6
# milk: 7                         - cheese: 8
# statistics                      - milk: 7
#                                 Total Products: 4
#                                 Total Quantity: 31



products = {}


while True:
    command = input()
    if command == "statistics":
        break

    product, quantity = command.split(": ")
    if product in products:
        products[product] += int(quantity)
    else :
        products[product] = int(quantity)

print("Products in stock:")

for key in products:
    print(f"- {key}: {products[key]}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")