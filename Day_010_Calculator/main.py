import os
from art import logo

def clear_console():
    if os.name == "nt": # OS is Windows
        os.system("cls")
    else:
        os.system("clear")
        
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    
    num1 = float(input("\nWhat's the first number?: "))
    should_continue = True

    while should_continue:

        for symbol in operations:
            print(f" " + f"{symbol}")
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))

        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"\n{num1} {operation_symbol} {num2} = {answer}\n")
        
        user_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.\nType 'exit' to exit the program: ").lower()
        if user_choice == "y":
            num1 = answer
        elif user_choice == "n":
            should_continue = False
            clear_console()
            calculator()
        else:
            should_continue = False
            print("\nGoodbye.\n")
            
calculator()