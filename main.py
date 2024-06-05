def add(n1, n2):
    """ Addition """
    return n1 + n2
def substract(n1, n2):
    """ Subtraction """
    return n1 - n2
def multiply(n1, n2):
    """ Multiplication """
    return n1 * n2

def divide(n1, n2):
    """ Division"""
    return n1 / n2

operators = ['+', '-', '*', '/']
def processing_calculation(number_1,number_2,operator):
    functions = {
        '+': add(number_1, number_2),
        '-': substract(number_1, number_2),
        '*': multiply(number_1, number_2),
        '/': divide(number_1, number_2)
    }
    return functions[operator]


def calculator():
    first_number = int(input("What's the first number?: "))
    checker = 'y'
    while checker == 'y':
        print(*[i for i in operators], sep='\n')
        operation = input("Pick an operation: ")
        second_number = int(input("What's the next number?: "))
        final_number = round(float(processing_calculation(number_1=first_number, number_2=second_number, operator=operation)), 1)
        print(float(first_number), operation, float(second_number), '=', final_number, sep=' ')
        checker = input(f"Type 'y' to continue with {final_number}, or type 'n' to start a new calculation: ")
        first_number = final_number

calculator() 