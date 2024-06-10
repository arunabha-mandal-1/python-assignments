# Write a program in Python to check whether a number is odd or even and also for prime number check.

# Whether number is odd or even
def is_odd_even(n):
    if n % 2 == 0:
        print(f"{n} is an even number.")
    else:
        print(f"{n} is an odd number.")

# Whether number is prime
def is_prime(n):
    if n <= 1:
        print(f"{n} is not a prime number.")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            return
    print(f"{n} is a prime number.")


a = -13
is_odd_even(a)
is_prime(a)