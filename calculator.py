"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculator():
    """
    calculates prefix notation expression

    returns calculated value
    """

    while True:
        result = None
        expression = input("Enter your equation > ")
        expression = expression.split(" ")
        

        if "q" in expression:
            print("You have exited the calculator.")
            return
        if len(expression) > 3:
            print("Invalid input, too many arguments")
            return
        if len(expression) < 2:
            print("Invalid input, too few arguments")
            return
        if not expression[1].isdigit() or not expression[2].isdigit():
             print("Invalid input, only digits accepted as arguments!")
             return

        if len(expression) == 2:
            expr1 = float(expression[1])
            if expression[0] == 'square':
                result = square(expr1)
                
            elif expression[0] == 'cube':
                result = cube(expr1)

        if len(expression) == 3:
            expr1 = float(expression[1])
            expr2 = float(expression[2])

            if expression[0] == 'pow':
                result = power(expr1, expr2)

            elif expression[0] == '+':
                result = add(expr1, expr2)

            elif expression[0] == '-':
                result = subtract(expr1, expr2)

            elif expression[0] == '*':
                result = multiply(expr1, expr2)

            elif expression[0] == '/':
                result = divide(expr1, expr2)

            elif expression[0] == 'mod':
                result = mod(expr1, expr2)  
                
        print(f"The result is: {result}")

calculator()