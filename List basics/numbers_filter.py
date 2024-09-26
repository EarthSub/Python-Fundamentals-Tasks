roll_num = int(input())
list_of_numbers = []

for _ in range(roll_num):
    current_number = int(input())
    list_of_numbers.append(current_number)

process = input()
processed_list_of_numbers = []

if process == "even":
    for num in list_of_numbers:
        if num % 2 == 0:
            processed_list_of_numbers.append(num)
elif process == "odd":
    for num in list_of_numbers:
        if num % 2 != 0:
            processed_list_of_numbers.append(num)
elif process == "negative":
    for num in list_of_numbers:
        if num < 0:
            processed_list_of_numbers.append(num)
elif process == "positive":
    for num in list_of_numbers:
        if num >= 0:
            processed_list_of_numbers.append(num)

print(processed_list_of_numbers)