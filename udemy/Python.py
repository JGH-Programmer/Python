def add(n1,n2):
    return n1+n2
def minus(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2





operations = {
    "+" : add,
    "-": minus,
    "/": divide,
    "*": multiply
}

num1 = int(input())
num2 = int(input())


for symbol in operations:
    print(symbol)
operation_symbol = input()

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)

print(answer)











