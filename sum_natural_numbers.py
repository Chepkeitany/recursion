'''
Sum the first n natural numbers
Time Complexity : O(n) - we make n recursive calls until we reach the base case
                         where n is the input natural number
Space Complexity: O(n) - the maximum recursive depth is n. Each recursive call
                         adds a new call stack frame
                         consuming additional space on the call stack
'''


def sum_numbers(n):
    """ Sum the first n natural numbers """
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


print(sum_numbers(5))
print(sum_numbers(3))
print(sum_numbers(1))
print(sum_numbers(0))
