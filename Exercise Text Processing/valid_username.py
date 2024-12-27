# Write a program that reads usernames on a single line (separated by ", ")
# and prints all valid usernames on separate lines.

# A valid username:

# · has length between 3 and 16 characters inclusive
# · can contain only letters, numbers, hyphens, and underscores
# · has no redundant symbols before, after, or in between


#                             Examples

# Input                                                       Output

# sh, too_long_username, !lleg@l ch@rs, jeffbutt              jeffbutt

# Jeff, john45, ab, cd, peter-ivanov, @smith                  Jeff
#                                                             John45
#                                                             peter-ivanov



def valid_username(name: str) -> bool:
    if not (3 <= len(name) <= 16):
        return False
    for letter in name:
        if not (letter.isalnum() or letter == "-" or letter == "_"):
            return False
    return True


usernames = input().split(", ")

for username in usernames:
    if valid_username(username):
        print(username)

