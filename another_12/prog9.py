# Write a python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]
print(s)