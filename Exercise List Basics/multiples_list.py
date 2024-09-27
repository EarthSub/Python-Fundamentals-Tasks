factor = int(input())
count = int(input())

the_list = []

for num in range(1, count + 1):
    the_list.append(num * factor)

print(the_list)