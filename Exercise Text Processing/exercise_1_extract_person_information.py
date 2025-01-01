# Write a program that reads N lines of strings and extracts the name and the age of a given person:

# · The person's name will be surrounded by "@" and "|" in the format "@{name}|".

# · The person's age will be surrounded by "#" and "*" in the format "#{age}*".

# Example: "Hello my name is @Peter| and I am #20* years old."

# For each found name-age pair, print a line in the following format "{name} is {age} years old."


#                             Example

# Input                                                   Output

# 2                                                       George is 18 years old.
# Here is a name @George| and an age #18*                 Billy is 35 years old.
# Another name @Billy| #35* is his age

# 3                                                       lilly is 5 years old.
# random name @lilly| random digits #5*age                Marry is 19 years old.
# @Marry| with age #19*                                   Garry is 48 years old.
# here Comes @ Garry | he is  # 48* years old


def name_searcher(some_string):
    the_name = ""
    spliter = some_string.split("@")
    searcher = spliter[1]
    for letter in searcher:
        if letter.isalpha():
            the_name += letter
        else:
            return the_name


def age_searcher(some_string):
    ages = ""
    spliter = some_string.split("#")
    searcher = spliter[1]
    for number in searcher:
        if number.isdigit():
            ages += number
    return ages


numbers_of_interactions = int(input())
for turn in range(numbers_of_interactions):
    initial_string = input()
    name = (name_searcher(initial_string))
    age = (age_searcher(initial_string))
    print(f"{name} is {age} years old.")
