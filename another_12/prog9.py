# Write a python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s = s2[0] + s1[1:] + " " + s1[0] + s2[1:]
print(s)