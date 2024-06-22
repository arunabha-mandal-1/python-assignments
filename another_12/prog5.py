# Write a program that accepts any number and prints the number of digits in that number.

num = input("Enter a number: ")
try:
    # handle for int
    i = int(num)
    print(f"Number of digits: {len(str(abs(i)))}")
except ValueError:
    try:
        # handle for float
        f = float(num)
        print(f"Number of digits: {len(str(abs(f))) - 1}")
    except ValueError:
        # handle other
        print("Enter int or float!!")

