# Write a program to concatenate two strings using recursion.

def concat(s1, s2):
    if(s1 == ""):
        return s2
    return s1[0] + concat(s1[1:], s2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s = concat(s1, s2)
print(s)
