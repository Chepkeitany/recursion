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

if __name__ == '__main__':
    assert sum_numbers(5) == 15, "Failed on sum_numbers(5)"
    assert sum_numbers(3) == 6,  "Failed on sum_numbers(3)"
    assert sum_numbers(1) == 1,  "Failed on sum_numbers(1)"
    assert sum_numbers(0) == 0,  "Failed on sum_numbers(0)"

    print("All tests passed!")
