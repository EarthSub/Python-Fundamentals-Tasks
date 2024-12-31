# You are given a collection of tickets separated by commas and spaces (one or many).
# You need to check each ticket to see if it has a winning combination of symbols:

# · A valid ticket has exactly 20 characters.
# · A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^'
#     uninterruptedly repeated at least 6 times in both halves of the tickets.
# · In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides

# An example of a valid winning ticket:

# "Cash$$$$$$Ca$$$$$$sh"

# An example of a Jackpot winning valid ticket:

# "$$$$$$$$$$$$$$$$$$$$"

# Input

# The input will be read from the console. The input consists of a single line containing all tickets separated by
# commas and one or more white spaces in the format:

# · "{ticket}, {ticket}, … {ticket}"

# Output

# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# · If the ticket is invalid: "invalid ticket"
# · If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
# · If the ticket is valid and winning, but not a Jackpot:
#     "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
# · If the ticket hits the Jackpot:
#     "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"

# Constraints

# · Number of tickets will be in range [0 … 100]


#                         Examples

# Input                                               Output

# Cash$$$$$$Ca$$$$$$sh                                ticket "Cash$$$$$$Ca$$$$$$sh" - 6$

# $$$$$$$$$$$$$$$$$$$$, aabb ,                        ticket "$$$$$$$$$$$$$$$$$$$$" - 10$ Jackpot!
# th@@@@@@eemo@@@@@@ey                                invalid ticket
#                                                     ticket "th@@@@@@eemo@@@@@@ey" - 6@

# validticketnomatch:(,                               ticket "validticketnomatch:(" - no match
# Cas$$$$$$$Ca$$$$$$s$                                ticket "Cas$$$$$$$Ca$$$$$$s$" - 6$



def winning_tickets(ticket):
    ticket = ticket.strip()
    if not len(ticket) == 20:
        print("invalid ticket")
    else:
        left_side_ticket = ticket[:10]
        right_side_ticket = ticket[10:]
        for current_symbol in winning_ticket_symbols:
            for matching_length in range(10, 5, -1):
                winning_symbols_repeating = current_symbol * matching_length
                if winning_symbols_repeating in left_side_ticket and winning_symbols_repeating in right_side_ticket:
                    if matching_length == 10:
                        print(f'ticket "{ticket}" - {matching_length}{current_symbol} Jackpot!')
                        return
                    print(f'ticket "{ticket}" - {matching_length}{current_symbol}')
                    return
        print(f'ticket "{ticket}" - no match')
        return



initial_data = input().split(",")
winning_ticket_symbols = ("@", "#", "$", "^")

for tickets in initial_data:
    winning_tickets(tickets)