'''
Generate the fibonacci sequence
Fibonacci sequence is characterized by the fact that every number after
the first two is the sum of the two preceding ones. It typically starts with 0 and 1.
The sequence goes like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 and so forth

# Brute force recursion fibonacci(n)
Time Complexity: O(2^n) where n is the input number
                        each recursive call generates two more calls, 
                        leading to an exponential growth
                        in the number of calls as n increases.
Space Complexity: O(n) this is because the maximum depth of the recursion is n

# Recursion with memoization
Time Complexity: O(n) - we calculate the nth fibonacci number from 0 to n only once
                        and store the values in the memoization_table for future use
Space Complexity: O(n) - this is because the memoization_table will store up to n values
                         also the recursion calls will consume the call stack up to n
'''

import time

def fibonacci(n):
    """ Compute the nth fibonacci number """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

memoization_table = {}
def fibonacci_memoized(n):
    """ Compute the nth fibonacci number """
    if n <= 1:
        return n

    if n in memoization_table:
        return memoization_table[n]
    memoization_table[n] = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    return memoization_table[n]


# Brute force recursive fibonacci sequence generation
start_time = time.time()
fibonacci_sequence = [fibonacci(i) for i in range(20)]
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Generating first 20 fibonacci numbers using brute force took: {elapsed_time} seconds")

assert fibonacci_sequence[0] == 0, "Failed on fibonacci_sequence[0]"
assert fibonacci_sequence[1] == 1, "Failed on fibonacci_sequence[1]"
assert fibonacci_sequence[3] == 2, "Failed on fibonacci_sequence[3]"

# Recursive fibonacci sequence generation using memoization
start_time = time.time()
fibonacci_sequence_memoized = [fibonacci_memoized(i) for i in range(20)]
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Generating first 20 fibonacci numbers with memoization took: {elapsed_time} seconds")
assert fibonacci_sequence[0] == 0, "Failed on fibonacci_sequence[0]"
assert fibonacci_sequence[1] == 1, "Failed on fibonacci_sequence[1]"
assert fibonacci_sequence[3] == 2, "Failed on fibonacci_sequence[3]"
print("All tests passed!")
