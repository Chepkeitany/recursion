'''
Calculate the Greatest Common Divisor(GCD) of two positive numbers
using the Euclidean algorithm
'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

assert gcd(12,18) == 6, "Failed on gcd(12,18)"
assert gcd(15,25) == 5, "Failed on gcd(15,25)"
assert gcd(1, 5) == 1,  "Failed on gcd(1, 5)"

print("All tests passed!")