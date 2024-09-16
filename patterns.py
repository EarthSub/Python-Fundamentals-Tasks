number = int(input())

for a in range(number+1):
    print("*" * a)
for b in range(number - 1, 0, -1):
    print("*" * b)