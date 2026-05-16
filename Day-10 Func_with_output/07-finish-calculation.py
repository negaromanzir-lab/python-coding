# deference between print and return

#calculator project
from art import calculator_logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}

def calculator():
    print(calculator_logo)

    num1 = float(input("What is the first number?: "))
    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what is the next number?: "))
        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to exit.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()