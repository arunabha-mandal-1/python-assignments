# Factorial of a number

def factorial(a):
    if (a < 0):
        print("Not defined!")
    elif (a < 2):
        print(f"Factorial of {a} is 1.")
    else:
        product = 1
        for i in range(1, a + 1):
            product  = product * i
        print(f"Factorial of {a} is {product}.")
    

a = int(input("Enter a number: "))
factorial(a)