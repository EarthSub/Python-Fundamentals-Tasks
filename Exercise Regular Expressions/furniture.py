# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".
# The price could be a floating-point or integer number. You should store the names of the furniture and the total price.
#
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
#
# "Bought furniture:

# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"


#                                 Examples

# Input                           Output                          Comment

# >>Sofa<<312.23!3                Bought furniture:               Only the Sofa and the TV are valid, for
# >>TV<<300!5                     Sofa                            each of them we multiply the price by
# >Invalid<<!5                    TV                              each of them we multiply the price by
# Purchase                        Total money spend: 2436.69


import re
bought_furniture = input()
pattern = r">>([A-Za-z]+)<<(\d+\.*\d*)!(\d+)"


total_price = 0
items = []
while bought_furniture != "Purchase":
    result = re.search(pattern, bought_furniture)
    if result:
        item, price, quantity = result.groups()
        total_price += float(price) * int(quantity)
        items.append(item)
    bought_furniture = input()

print("Bought furniture:")
for item in items:
    print(item)
print(f"Total money spend: {total_price:.2f}")

