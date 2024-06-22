# Write a program to print the following patterns:
# 1. 
# $ * * * *
# * $ * * *
# * * $ * *
# * * * $ *
# * * * * $

# 2.
#  1 2 3 4 5
#1 $ * * * $
#2 * $   $ *
#3 *   $   *
#4 * $   $ *
#5 $ * * * $

def print_pattern_1(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if(j == i):
                print("$", end=" ")
            else:
                print("*", end=" ")
        print()

def print_pattern_2(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if(j == i):
                print("$", end=" ")
            elif (i + j) == n + 1:
                print("$", end=" ")
            elif ((1 < i < n) and (1 < j < n)) and ((i + j) == n or (i + j) == n + 2):
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()

print_pattern_2(5)