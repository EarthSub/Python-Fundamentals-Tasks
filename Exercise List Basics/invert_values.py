numbers = input()
numbers_list = [int(x) for x in numbers.split(" ")]
opposite_numbers_list = []
for num in numbers_list:
    if num > 0:
        num = -abs(num)
        opposite_numbers_list.append(num)
    else:
        num = abs(num)
        opposite_numbers_list.append(num)

print(opposite_numbers_list)

# print([-int(num) for num in input().split()])