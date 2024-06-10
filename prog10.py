# 99 has the property (9 * 9) + (9 + 9) = 99. How many numbers have this property below 1000.
import math

def has_property(n):
    digits = [int(d) for d in str(n)]
    digit_product = math.prod(digits)
    digit_sum = sum(digits)
    return n == (digit_product + digit_sum)

list = []
count = 0
for i in range(10, 1000):
    if has_property(i):
        count = count + 1
        list.append(i)

print(f"{count} numbers have the mentioned property.")
print(list)