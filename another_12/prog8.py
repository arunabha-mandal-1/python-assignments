# Write a program to compute F(n, r) where F(n, r) can be recursively defined as F(n, r) = F(n-1, r) + F(n-1, r-1).
def F(n, r):
    # Base case is assumed
    if r == 0 or r == n:
        return 1
    elif n < r:
        return -1
    return F(n-1, r) + F(n-1, r-1)

# Example usage:
n = int(input("Enter n: "))
r = int(input("Enter r: "))
result = F(n, r)
print(f"F({n}, {r}) = {result}")