# Calculator

from art import logo
import os

# Addition
def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

# dictionary to store the operators
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    # Print each operation from operations dictionary
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the options above: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    previous_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {previous_answer}")

    # Subsequent operations..
    should_continue = True
    while should_continue:
        choice = input(f"Type 'y' to continue calculating with {previous_answer}, or type 'n' to to start a new calculation.: ")

        if choice == "n":
            should_continue = False
            os.system('cls')
            calculator()

        operation_symbol = input("Pick an operation: ")
        num3 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        current_answer = calculation_function(previous_answer, num3)
        print(f"{previous_answer} {operation_symbol} {num3} = {current_answer}")
        previous_answer = current_answer

calculator()