# Write a program to input a decimal number and print the decimal part of the number.

number = float(input("Enter a decimal number: "))
print(f"Decimal part of {number} is {round(number - int(number), 3)}")