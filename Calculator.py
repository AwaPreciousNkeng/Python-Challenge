# Calculator
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    if n2 == 0:
        return "Math Error!"
    else:
        return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
finished_calculating = False
num1 = int(input("What's your first number: "))
for symbol in operations:
        print(symbol)
while not finished_calculating:
    operation_symbol = input("Pick your operation from the line above: ")
    num2 = int(input("What's the next number: "))
    calculation_function = operations[operation_symbol]
    
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}") 

    should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if should_continue.lower() == 'n':
        finished_calculating = True
    elif should_continue.lower() == 'y':
        num1 = answer
    else:
        print("Invalid Input!") 


