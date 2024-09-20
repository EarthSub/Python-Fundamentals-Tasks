divisor = int(input())
boundary = int(input())

if divisor > 0:
    for divisible in range(boundary, divisor-1, -1):
        if divisible % divisor == 0:
            break
print(divisible)