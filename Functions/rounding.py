# Write a program that rounds all the given numbers, separated by a single space,
# and prints the result as a list. Use round().
#
#                  Example
#
#      Input                    Output
#
# 1.0 2.5 3.0 4.5            [1, 2, 3, 4]
#
# 2.56 1.9 -3.4 8.1          [3, 2, -3, 8]





def rounding(the_list):
    return [round(x) for x in the_list]



current_list = input().split()
current_list_floated = [float(x) for x in current_list]

print(rounding(current_list_floated))