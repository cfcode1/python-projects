
def add(x, y):
    return int(x) + int(y)


def subtract(x, y):
    return int(x) - int(y)


def multiply(x, y):
    return int(x) * int(y)


def divide(x, y):
    return int(x) / int(y)

def exp(x, y):
    return int(x)**int(y)

while True:
    var = input("Enter a Number: ")
    method = input("Choose an option:\nAdd + \nSubtract - \nMultiply x \nDivide / \n ")
    var2 = input("Enter a second number: ")

    print("The answer is: ")
    if method == "+":
        print(add(var, var2))
    elif method == "-":
        print(subtract(var, var2))
    elif method == "x":
        print(multiply(var, var2))
    elif method == "/":
        print(divide(var, var2))