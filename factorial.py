'''
Compute the factorial of a positive number
Time Complexity : O(n) - we make n recursive calls until we reach the base case
                         where n is the input
Space Complexity: O(n) - the maximum recursive depth is n. Each recursive call
                         adds a new call stack frame
                         consuming additional space on the call stack
'''
def factorial(n):
    if n < 0:
        raise ValueError("Factorial can only be computed for non-negative numbers!")
    elif n <= 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(5))
    print(factorial(1))
    print(factorial(0))
