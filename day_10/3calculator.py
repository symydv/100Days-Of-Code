#CALCULATOR


def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    n1 = float( input("Enter n1:"))

    for symbol in operation :
        print(symbol)

    should_continue = True


    while should_continue == True:

        operation_symbol = input("pick an operation from line above:")

        n2 = float(input("Enter n2:"))

        calculation_function = operation[operation_symbol]
        ans = calculation_function(n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {ans}")

        if input(f"type 'y' to continue calc with {ans}, type 'n' to start a new calculation: ") == "y":
            n1 = ans
        else:
            should_continue = False
            calculator() #it is called recursion when we call a function in itself


calculator()

    



