# CLI based calculator
import os


def spaces():
    print(' ')


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


clearConsole()


def display():
    print("---------------------------------------")
    print("            Calculator")
    print("---------------------------------------")
    spaces()


def restart():
    displayoperator()
    operator_choice()
    take_input()
    checking()


def displayoperator():
    print("1. Addition(+) 2. Subtraction(-) \n 3. multiplication(*) 4. Division(/)")
    spaces()


def operator_choice():
    global operator
    operator = (input("Enter the operator of your selection "))
    spaces()


def addition(num_one, num_two):
    return num_one + num_two


def subtraction(num_one, num_two):
    return num_one - num_two


def multiplication(num_one, num_two):
    return num_one * num_two


def division(num_one, num_two):
    return num_one / num_two


def take_input():
    global number_first
    global number_second
    spaces()
    number_first = int(input("Enter the first number "))
    spaces()
    number_second = int(input("Enter the second number"))


def checking():
    if operator == "1":
        print(addition(number_first, number_second))
        spaces()
    elif operator == "2":
        print(subtraction(number_first, number_second))
        spaces()
    elif operator == "3":
        print(multiplication(number_first, number_second))
        spaces()
    elif operator == "4":
        print(division(number_first, number_second))
        spaces()
    else:
        print("Invalid operator")
        spaces()


def if_restart():

    restart_calculation = input(
        "Do you want to perform another calculation y/n")
    spaces()
    if restart_calculation == "y":
        clearConsole()
        restart()
        if_restart()
    else:
        spaces()
        print("Thanks for using the calculator")
    while restart_calculation != 'n':
        clearConsole()
        restart()
        if_restart()


        # calling functions
display()
displayoperator()
operator_choice()
take_input()
checking()
if_restart()
