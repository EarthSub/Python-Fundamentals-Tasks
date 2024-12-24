# The force users struggle to remember which side is the different force users from because they switch them too often.
# So you are tasked to create a web application to manage their profiles.
# You should store information for every unique force user registered in the application.

# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"

# The "force_user" and "force_side" are strings, containing any character.

# If you receive "force_side | force_user":

# · If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
# · Only if there is no such force user in any force side -> add the force user to the corresponding side.
# · If there is such force user already -> skip the command and continue to the next operation.

# If you receive a "force_user -> force_side":

# · If there is such force user already -> change their side.
# · If there is no such force user in any force side -> add the force user to the corresponding force side.
# · If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
# · Then you should print on the console: "{force_user} joins the {force_side} side!".

# You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side.
# For each side, print the force users.

# In case there are no forced users on a side, you shouldn't print the side information.

# Input / Constraints

# · The input comes in the form of commands in one of the formats specified above.
# · The input ends when you receive the command "Lumpawaroo".

# Output

# · As output for each force side, you must print all the force users.
# · The output format is:

# "Side: {force_side}, Members: {force_users_count}

# ! {force_user1}
# ! {force_user2}
# …
# ! {force_userN}"
# · In case there are NO force users on a side, don't print this side.


#                                         Examples

# Input                                   Output                                      Comments

# Light | Peter                           Side: Light, Members: 1                     We register Peter on the
# Dark | Kim                              ! Peter                                     Light side and Kim on the
# Light | Kim                             Side: Dark, Members: 1                      Dark side. After receiving
# Lumpawaroo                              ! Kim                                       "Lumpawaroo", we print
#                                                                                     both sides.

# Lighter | Royal                         Ivan Ivanov joins the Lighter side!         Although Ivan Ivanov doesn't
# Darker | DCay                           DCay joins the Lighter side!                have a profile, we register
# Ivan Ivanov -> Lighter                  Side: Lighter, Members: 3                   him and add him to the
# DCay -> Lighter                         ! Royal                                     Lighter side.
# Lumpawaroo                              ! Ivan Ivanov                               We remove DCay from the
#                                         ! DCay                                      Darker side and add him to
#                                                                                     the Lighter side.
#                                                                                     We print only the Lighter
#                                                                                     side because the Darker side
#                                                                                     has no members.


def side_user(side, user):
    user_exists = False
    for users in force_book.values():
        if user in users:
            user_exists = True
            break
    if not user_exists:
        if side not in force_book.keys():
            force_book[side] = []
        force_book[side].append(user)



def user_side(user, side):
    for users in force_book.values():
        if user in users:
            users.remove(user)
            break
    if side not in force_book.keys():
        force_book[force_side] = []
    force_book[force_side].append(user)
    print(f"{user} joins the {side} side!")



force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:
        force_side, force_user = command.split(" | ")
        side_user(force_side, force_user)
    else:
        force_user, force_side = command.split(" -> ")
        user_side(force_user, force_side)


for force_side, force_users in force_book.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for usr in force_users:
            print(f"! {usr}")



