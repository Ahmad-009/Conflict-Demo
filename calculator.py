def add(a, b):
    print("Adding symbols")
    return a + b

def subtract(a, b):
    print('substracting the symbols')
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Calculator ready!")
