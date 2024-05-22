# Write a program to ask the user for a string and print the location of each 'a' in the string

s = str(input("Enter a string : "))
s = str.lower(s)
for i in range(len(s)):
    if(s[i] == 'a'):
        print(i)
