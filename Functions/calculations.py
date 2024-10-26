# Create a function that receives three parameters,
# calculates a result depending on the given operator, and returns it.
# Print the result of the function.
#
# The input comes as three parameters – an operator as a string
# and two integer numbers. The operator can be one of the following:
# "multiply", "divide", "add", and "subtract".



def calculator(operation: str, first_number: int, second_number: int):
    if operation == "add":
        return first_number + second_number
    elif operation == "subtract":
        return first_number - second_number
    elif operation == "multiply":
        return first_number * second_number
    elif operation == "divide":
        return int(first_number / second_number)



operator = input()
first_number = int(input())
second_number = int(input())


result = calculator(operator, first_number, second_number)

print(result)
