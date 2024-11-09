# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line.


#                         Example
#
# Input                                           Output
#
# arp, live, strong
# lively, alive, harp, sharp, armstrong           ['arp', 'live', 'strong']
# tarp, mice, bull
#
# lively, alive, harp, sharp, armstrong            []





string_as_list_one = input().split(", ")
string_as_list_two = input().split(", ")

new_list = []

for word in string_as_list_one:
    for n_word in string_as_list_two:
        if word in n_word:
            new_list.append(word)
            break

print(new_list)