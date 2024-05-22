# Write a program to find how many numbers between 1 to 100 contain digit 3

def whether_contains_3(limit):
    count = 0

    # Test purpose
    set1 = set() # Included numbers

    for i in range(1, limit + 1):
        if '3' in str(i):
            set1.add(i)
            count += 1

    print(set1)
    return count

limit = 100
print(f"{whether_contains_3(limit)} numbers between 1 - {limit} contain digit 3.")