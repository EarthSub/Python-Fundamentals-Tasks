# SoftUni just got a new fancy parking lot. It even has online parking validation,
# except the online service doesn't work. It can only receive users' data, but it doesn('t know what to do with it.
# Good thing you')re on the dev team and know how to fix it, right?

# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.

# The program receives 2 types of commands:
#     · "register {username} {license_plate_number}":
#         o The system only supports one car per user at the moment,
#            so if a user tries to register another license plate using the same username, the system should print:
#            "ERROR: already registered with plate number {license_plate_number}"
#         o If the check above passes successfully, the user should be registered, so the system should print:
#         "{username} registered {license_plate_number} successfully"

#     · "unregister {username}":
#         o If the user is not present in the database, the system should print: "ERROR: user {username} not found"
#         o If the check above passes successfully, the system should print: "{username} unregistered successfully"

# After you execute all of the commands, print all the currently registered users and their license plates in the format:

#     · "{username} => {license_plate_number}"

# Input

#     · First line: n - number of commands - integer
#     · Next n lines: commands in one of the two possible formats:
#         o Register: "register {username} {license_plate_number}"
#         o Unregister: "unregister {username}"

# The input will always be valid, and you do not need to check it explicitly.


#                     Examples

# Input                                       Output

# 5                                           John registered CS1234JS successfully
# register John CS1234JS                      George registered JAVA123S successfully
# register George JAVA123S                    Andy registered AB4142CD successfully
# register Andy AB4142CD                      Jesica registered VR1223EE successfully
# register Jesica VR1223EE                    Andy unregistered successfully
# unregister Andy                             John => CS1234JS
#                                             George => JAVA123S
#                                             Jesica => VR1223EE

# 4                                           Jony registered AA4132BB successfully
# register Jony AA4132BB                      ERROR: already registered with plate number AA4132BB
# register Jony AA4132BB                      Linda registered AA9999BB successfully
# register Linda AA9999BB                     Jony unregistered successfully
# unregister Jony                             Linda => AA9999BB

# 6                                           Jacob registered MM1111XX successfully
# register Jacob MM1111XX                     Anthony registered AB1111XX successfully
# register Anthony AB1111XX                   Jacob unregistered successfully
# unregister Jacob                            Joshua registered DD1111XX successfully
# register Joshua DD1111XX                    ERROR: user Lily not found
# unregister Lily                             Samantha registered AA9999BB successfully
# register Samantha AA9999BB                  Anthony => AB1111XX
#                                             Joshua => DD1111XX
#                                             Samantha => AA9999BB

def registered(user_name, registration_number):
    if user_name in softuni_parking:
        return print(f"ERROR: already registered with plate number {registration_number}")
    softuni_parking[user_name] = registration_number
    return print(f"{user_name} registered {registration_number} successfully")


def unregistered(user_name):
    if user_name not in softuni_parking:
        return print(f"ERROR: user {user_name} not found")
    del softuni_parking[user_name]
    return print(f"{user_name} unregistered successfully")


softuni_parking = {}

passing = int(input())


for passed in range(passing):
    action = input().split()
    if action[0] == "register":
        name = action[1]
        reg_number = action[2]
        registered(name, reg_number)
    elif action[0] == "unregister":
        name = action[1]
        unregistered(name)

for u_name in softuni_parking:
    print(f"{u_name} => {softuni_parking[u_name]}")