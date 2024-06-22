# Write a function to convert a given string to all uppercase 
# if it contains at least 2 uppercase characters in the first 4 characters.

def func(s):
    uc_count = len([ch for ch in s[:4] if ch.isupper()])
    if uc_count > 1:
        return s.upper()
    return s

s = input("Enter a string: ")
new_s = func(s)
print(new_s)