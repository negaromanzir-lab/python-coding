#calculator project
from art import calculator_logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(calculator_logo)

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

num1 = float(input("What is the first number?: "))
for operation in operations:
    print(operation)
operation_symbol = input("Pick an operation from the line above: ")
num2 = float(input("what is the second number?: "))
calculate_function = operations[operation_symbol]
answer = calculate_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")