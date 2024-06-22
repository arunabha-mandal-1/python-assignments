# Write a program to sum the series 1^2/1 + 2^2/2 + ..... + n^2/n

def sum_series(n):
    return sum(i**2/i for i in range(1, n+1))

n = int(input("Enter a number: "))
print(f"Sum of the series: {sum_series(n)}")