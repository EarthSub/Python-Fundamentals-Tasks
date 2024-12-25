# Write a program that reads a sequence of strings, separated by a single space.
# Each string should be repeated N times, where N is the length of the string.
# Print the final strings concatenated into one string.


#           Examples

# Input                   Output

# hi abc add              hihiabcabcabcaddaddadd

# work                    workworkworkwork

# ball                    ballballballball

data = input().split()
new_data = [text * len(text) for text in data]
print("".join(new_data))