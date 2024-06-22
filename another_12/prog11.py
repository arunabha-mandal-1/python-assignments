# Write a function to get a string made of its first three characters of a specified string. 
# If the length of the string is less than 3, then return the original string.

def first_three_chars(s):
    if len(s) < 3:
        return s
    else:
        return s[:3]
    
s = input("Enter a string: ")
print(f"Resulting string: {first_three_chars(s)}")