'''
Given an integer x and power n, raise x to the power of n
'''

def power(x, n):
    """
    Calculate x raised to the power of n.
    """
    # Base case: any number to the power of 0 is 1
    if n == 0:
        return 1
    # If exponent is negative, use the reciprocal of the base
    if n < 0:
        return 1 / power(x, -n)
    half_power = float(power(x, n // 2))
    # If n is even, the result if half_power squared
    if n % 2 == 0:
        return half_power * half_power
    # If n is odd, multiply the base with half_power squared
    return x * half_power * half_power

if __name__ == '__main__':
    assert power(10, 2) == 100,  "Failed on power(10,2)"
    assert power(5, 0)  == 1.0,  "Failed on power(5, 0)"
    assert power(2, 5)  == 32.0, "Failed on power(2, 5)"

    print("All tests passed!")
