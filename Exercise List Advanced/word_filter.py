# Using comprehension, write a program that receives some text, separated by space,
# and takes only those words whose length is even. Print each word on a new line.


#               Examples

# Input                           Output

# kiwi orange banana apple        kiwi
#                                 orange
#                                 banana



# pizza cake pasta chips          cake



starting_list = input().split()
filtered_list = [print(word) for word in starting_list if len(word) % 2 == 0]
