'''
Compute the factorial of a positive number
Time Complexity : O(n) - we make n recursive calls until we reach the base case
                         where n is the input
Space Complexity: O(n) - the maximum recursive depth is n. Each recursive call
                         adds a new call stack frame
                         consuming additional space on the call stack
'''


def factorial(n):
    """ Compute the factorial of a positive number """
    if n < 0:
        raise ValueError(
            "Factorial can only be computed for non-negative numbers!")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


assert factorial(5) == 120, "Failed on factorial(5)"
assert factorial(1) == 1, "Failed on factorial(1)"
assert factorial(0) == 1, "Failed on factorial(0)"

print("All tests passed!")
