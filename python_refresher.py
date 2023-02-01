
# Simple python calculator
print("Welcome to the python calculator!")

# grabs input for two numbers
number1 = input("Enter your first number: ")
number2 = input("Enter your second number: ")

# have user enter operator
print("Enter your operator. Choose one of the following: + - * /")
operator = input()

# a function to handle calculating
def calculator(num1, num2, operator):
    # empty variable to hold values
    equals = None
    # conditional logic for calculating
    if operator == "+":
        # convert num1 and num2 into int -- input is a string
        equals = int(num1) + int(num2)
    elif operator == "-":
        equals = int(num1) - int(num2)
    elif operator == "/":
        equals = int(num1) / int(num2)
    elif operator == "*":
        equals = int(num1) * int(num2)
    else:
        equals = "Not a valid operator. Please try again"
    return equals

print(calculator(number1, number2, operator))