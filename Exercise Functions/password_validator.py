# Write a function that checks if a given password is valid. Password validations are:

# · It should be 6 - 10 (inclusive) characters long

# · It should consist only of letters and digits

# · It should have at least 2 digits

# If a password is valid, print "Password is valid".

# Otherwise, for every unfulfilled rule, print a message:

# · "Password must be between 6 and 10 characters"

# · "Password must consist only of letters and digits"

# · "Password must have at least 2 digits"


#         Examples

# Input               Output
#
# logIn               Password must be between 6 and 10 characters
#                     Password must have at least 2 digits



# MyPass123           Password is valid




# Pa$s$s              Password must consist only of letters and digits
#                     Password must have at least 2 digits


def length(psw: str) -> bool:
    return 6 <= len(psw) <= 10


def letter_and_digits(psw: str) -> bool:
    return psw.isalnum()


def digits(psw: str) -> int:
    counter = 0
    for digit in psw:
        if digit.isdigit():
            counter += 1
    return counter


def password_validator():
    if not length(password):
        print("Password must be between 6 and 10 characters")
    if not letter_and_digits(password):
        print("Password must consist only of letters and digits")
    if digits(password) < 2:
        print("Password must have at least 2 digits")
    if length(password) and (letter_and_digits(password) == True) and digits(password) >= 2:
        print("Password is valid")


password = input()
password_validator()
