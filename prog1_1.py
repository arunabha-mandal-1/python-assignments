# Write a program to count how many integers from 1-1000 are not perfect squares, cubes and fifth powers.
print(f"{1000 - int(1000 ** (1/2))} numbers are not perfect square from 1-1000")
print(f"{1000 - int(1000 ** (1/3))} numbers are not perfect cube from 1-1000")
print(f"{1000 - int(1000 ** (1/5))} numbers are not perfect 5th power from 1-1000")