# Write a program to count how many integers from 1-1000 are not perfect squares, cubes and fifth powers.
import math


def count_non_perfect_powers(limit):
    excluded_numbers = set()
    included_numbers = set()

    # Exclude perfect squares
    for i in range(1, int(limit**0.5) + 1):
        excluded_numbers.add(int(math.pow(i, 2)))

    # Exclude perfect cubes
    for i in range(1, int(limit**(1/3)) + 1):
        excluded_numbers.add(int(math.pow(i, 3)))

    # Exclude perfect fifth powers
    for i in range(1, int(limit**(1/5)) + 1):
        excluded_numbers.add(int(math.pow(i, 5)))

    count_non_perfect_powers = 0
    for i in range(1, limit + 1):
        if i not in excluded_numbers:
            included_numbers.add(i)
            count_non_perfect_powers += 1

    # Print both sets
    print("Included numbers: ")
    print(included_numbers)
    print("Excluded numbers: ")
    print(excluded_numbers)

    return count_non_perfect_powers


limit = 100
print(
    f"Numbers of non-perfect powers within {limit} is {count_non_perfect_powers(limit)}")
