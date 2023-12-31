'''
Calculate the Greatest Common Divisor(GCD) of two positive numbers
using the Euclidean algorithm
'''

def gcd(a, b):
    if not(isinstance(a, int) and isinstance(b, int) and a > 0 and b > 0):
        raise ValueError("Inputs must be two positive numbers")
    
    def gcd_recursive(a, b):
        if b == 0:
            return a
        return gcd_recursive(b, a % b)

    return gcd_recursive(a, b)

assert gcd(12,18) == 6, "Failed on gcd(12,18)"
assert gcd(15,25) == 5, "Failed on gcd(15,25)"
assert gcd(1, 5) == 1,  "Failed on gcd(1, 5)"

# Test with negative input
try:
    gcd(-1, 5)
    assert False, "ValueError not raised for gcd(-1,5)"
except ValueError:
    pass # The input has been handled correctly

print("All tests passed!")
