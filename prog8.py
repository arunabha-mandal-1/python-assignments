# Find the square root value of a quadratic equation (find out for both real and imaginary parts).

def find_roots(a, b, c):
    # discriminant
    d = b**2 - 4*a*c
    if (d == 0):  # when d=0
        return [-(b/(2*a)), -(b/(2*a))]
    elif (d > 0):  # when d > 0
        root1 = round((-b + round(d**(1/2), 2)) / (2*a), 2)
        root2 = round((-b - round(d**(1/2), 2)) / (2*a), 2)
        return [root1, root2]
    else:  # when d < 0
        d = -d
        root1 = f"(-{b}-{round(d**(1/2), 2)}j)/{2*a}"
        root2 = f"(-{b}+{round(d**(1/2), 2)}j)/{2*a}"
        return [root1, root2]
    
a, b, c = 1, 9, 2
roots = find_roots(a, b, c)
print(roots)