# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:

# · If you have the product, print "We have {quantity} of {product} left".
# · Otherwise, print "Sorry, we don't have {product}".

#                         Example

# Input                                               Output

# cheese 10 bread 5 ham 10 chocolate 3                Sorry, we don't have jam
# jam cheese ham tomatoes                             We have 10 of cheese left
#                                                     We have 10 of ham left
#                                                     Sorry, we don't have tomatoes

# eggs 5 bread 10                                     We have 10 of bread left
# bread eggs                                          We have 5 of eggs left



stock = input().split()

product_dict = {}

for x in range(0, len(stock), 2):
    product = stock[x]
    quantity = stock[x + 1]
    product_dict[product] = int(quantity)

search = input().split()

for prod in search:
    if prod in product_dict:
        print(f"We have {product_dict[prod]} of {prod} left")
    else:
        print(f"Sorry, we don't have {prod}")