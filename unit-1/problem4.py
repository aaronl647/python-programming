#defining a function
def add(x , y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y



my_equation = input("What calculation would you like to do? (add, sub, mult, div) ")
val1 = int(input("What is the first number? "))
val2 = int(input("What is the second number? "))

if my_equation == "add":
    print(add(val1, val2))
elif my_equation == "sub":
    print(sub(val1, val2))
elif my_equation == "mult":
    print(mult(val1, val2))
elif my_equation == "div":
    print(div(val1, val2))

