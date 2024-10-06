numbers = input().split()
string = input()
string_list = list(string)

phrase = ""

for num in numbers:
    index = 0
    for digit in num:
        index += int(digit)
    index = index % len(string_list)
    phrase += string_list[index]
    string_list.pop(index)

print(phrase)