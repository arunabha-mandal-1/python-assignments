# Write a program to input a string and check whether the input string starts with a letter or not.

import string

s = str(input("Enter a string: "))
if len(s) > 0 and s[0] in string.ascii_letters:
    print("Starts with a letter")
else:
    print("Does not start with a letter")