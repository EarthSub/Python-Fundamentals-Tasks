starting_year = int(input())

while True:

    starting_year += 1
    starting_year_string = str(starting_year)
    if len(set(starting_year_string)) == len(starting_year_string):
        break
print(starting_year)