from art import logo

#Calculator

#Add
def add(n1,n2):
    return n1+n2

#Subtract
def subtract(n1,n2):
    return  n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return  n1/n2

operations = {}
operations['+'] = add
operations['-'] = subtract
operations['*'] = multiply
operations['/'] = divide
# print(operations)
def calculator():
    num1 = float(input("What's the first number?"))
    for operator in operations:
        print(operator)
    should_continue = True
    result = num1
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num3 = float(input("What's the next number?"))
        final_result = operations[operation_symbol](result,num3)
        print(f"{result} {operation_symbol} {num3} = {final_result}")
        result = final_result
        continue_operation = input(f"Type 'y' to continue calculating with {result}, ot type 'n' to exit.: ")
        if continue_operation == 'y':
            result = final_result
        else:
            should_continue = False
            calculator()

print(logo)
calculator()