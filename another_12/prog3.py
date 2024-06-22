# Write a program that prompts the user to enter a string. 
# The program calculates and displays the length of the string until the user enters "QUIT".

while True:
    s = input("Enter a string(Enter QUIT to quit): ")
    if s.upper() == "QUIT":
        break
    print(f"The length of the string is: {len(s)}")