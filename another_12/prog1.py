# Write a program that counts the number of digits, uppercase characters, and lowercase characters entered.

def count_characters(s):
    digits, uppercase, lowercase = 0, 0, 0
    for c in s:
        if c.isdigit(): digits = digits + 1
        elif c.isupper(): uppercase = uppercase + 1
        elif c.islower(): lowercase = lowercase + 1
    return digits, uppercase, lowercase

s = input("Enter a string: ")
digits, uppercase, lowercase = count_characters(s)
print(f"Digits: {digits}, uppercase: {uppercase}, lowercase: {lowercase}")