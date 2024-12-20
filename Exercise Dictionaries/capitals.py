# Using dictionary comprehension, write a program that receives country names on the first line,
# separated by comma and space ", ", and their corresponding capital cities on the second line
# (again separated by comma and space ", "). Print each country with its capital on a separate line in
# the following format: "{country} -> {capital}".

# Hints
# · You could use the zip() method.

#                         Examples

# Input                                               Output

# Bulgaria, Romania, Germany, England                 Bulgaria -> Sofia
# Sofia, Bucharest, Berlin, London                    Romania -> Bucharest
#                                                     Germany -> Berlin
#                                                     England -> London

# Bulgaria, Germany, France                           Bulgaria -> Varna
# Varna, Frankfurt, Paris                             Germany -> Frankfurt
#                                                     France -> Paris



list_of_countries = input().split(", ")
list_of_cities = input().split(", ")

both_dict = dict(zip(list_of_countries, list_of_cities))

#ditc_of_both = dict(ditc_of_both)

for country in both_dict:
    print(f"{country} -> {both_dict[country]}")