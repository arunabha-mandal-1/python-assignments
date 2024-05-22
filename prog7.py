# Write a program to input a string and double each character

s = str(input("Enter a string: "))
new_s = "".join(ch*2 for ch in s)
print(new_s)