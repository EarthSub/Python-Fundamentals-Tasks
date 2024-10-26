# Write a function that receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.




string =input()
counter = int(input())

#repeat_string = lambda a, b: a * b
def repeat_string(a, b):
    return a * b


result = repeat_string(string, counter)
print(result)