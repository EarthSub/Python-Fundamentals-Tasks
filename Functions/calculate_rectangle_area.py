# Create a function that calculates and returns the area of a rectangle by a given width and height.
# Print the result on the console.


def area(a: int, b: int) -> int:
    return a * b



first_side = int(input())
second_side = int(input())

result = area(first_side, second_side)
print(result)