# Create a class Catalogue. The __init__ method should accept the name of the catalogue (string).
# Each catalogue should also have an attribute called products, an empty list. The class should also have three more methods:

# · add_product(product_name: str) - adds the product to the products' list

# · get_by_letter(first_letter: str) - returns a list containing only the products that start with the given letter

# · __repr__ - returns the catalogue info in the following format: \
#     ("Items in the {name} catalogue: "
#      "{item1} "
#      "{item2})
#      …
#      {itemN}""
#      " The items should be sorted alphabetically in ascending order.


#                             Example

#     Test Code                                       Output

# catalogue = Catalogue("Furniture")                  ["Chair", "Carpet"]
# catalogue.add_product("Sofa")                       Items in the Furniture catalogue:
# catalogue.add_product("Mirror")                     Carpet
# catalogue.add_product("Desk")                       Chair
# catalogue.add_product("Chair")                      Desk
# catalogue.add_product("Carpet")                     Mirror
# print(catalogue.get_by_letter("C"))                 Sofa
# print(catalogue)


class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self):
        returning_string = f"Items in the {self.name} catalogue:\n"
        returning_string += "\n".join(sorted(self.products))
        return  returning_string



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

