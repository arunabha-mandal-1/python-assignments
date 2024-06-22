# Write a function that takes a list of words and returns the length of the longest one.

def longest_string_len(str_list):
    return max([len(word) for word in str_list])

str_list = ["kittu", "arunabha", "samrat", "kushal", "babai"]
l = longest_string_len(str_list)
print(f"Length of the longest string: {l}")