# You will receive a single input line containing strings, separated by spaces.
# The strings may contain any ASCII character except whitespace.
# Then you will begin receiving commands in one of the following formats:

# · merge {startIndex} {endIndex}
# · divide {index} {partitions}

# Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex.
# In other words, you should concatenate them. Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}

# If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.

# Every time you receive the divide command, you must divide the element at the given index into several small substrings
# with equal length. The count of the substrings should be equal to the given partitions.

# Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
# If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal lengths
# and make the last one - the longest.

# Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
# The input ends when you receive the command "3:1". At that point, you must print the resulting elements, joined by a space.


# Input

# · The first input line will contain the array of data.
# · On the next several input lines, you will receive commands in the format specified above.
# · The input ends when you receive the command "3:1".

# Output
# · As output, you must print a single line containing the elements of the array, joined by a space.

# Constraints

# · The strings in the array may contain any ASCII character except whitespace.
# · The startIndex and the endIndex will be in the range [-1000…1000].
# · The endIndex will always be greater than the startIndex.
# · The index in the divide command will always be inside the array.
# · The partitions will be in the range [0…100].
# · Allowed working time/memory: 100ms / 16MB.


#                     Examples

# Input                                       Output

# Ivo Johny Tony Bony Mony                    IvoJohnyTonyBonyMony
# merge 0 3
# merge 3 4
# merge 0 3
# 3:1

# abcd efgh ijkl mnop qrst uvwx yz            abcd efgh ijkl mnop qr st uv wx yz
# merge 4 10
# divide 4 5
# 3:1


data_list = input().split()

while True:
    command = input().split()
    if command[0] == "3:1":
        break
    if command[0] == "merge":
        start_index = max(0, int(command[1]))
        end_index = min(len(data_list), int(command[2]))
        data_list[start_index: end_index + 1] = ["".join(data_list[start_index: end_index + 1])]
    elif command[0] == "divide":
        index = int(command[1])
        pieces = int(command[2])
        current_string = data_list[index]
        start = 0
        step = len(current_string) // pieces
        remainder = len(current_string) % pieces
        list_with_steps = []
        if remainder:
            pieces -= 1
        for x in range(pieces):
            end = start + step
            list_with_steps.append(current_string[start:end])
            start = end
        if remainder:
            list_with_steps.append(current_string[start:])
        data_list = data_list[:index] + list_with_steps + data_list[index + 1:]

print(' '.join(data_list))
