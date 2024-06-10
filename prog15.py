# Write a program to enter a string and remove vowels from the string

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    new_s = "".join([ch for ch in s if ch not in vowels])
    return new_s

s = "Hello world!!"
print(remove_vowels(s))