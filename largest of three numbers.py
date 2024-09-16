first_number = int(input())
second_number = int(input())
third_number = int(input())
largest = 0

if first_number >= second_number and first_number >= third_number:
    largest = first_number
elif second_number >= first_number and second_number >= third_number:
    largest = second_number
else:
    largest = third_number

print(largest)

