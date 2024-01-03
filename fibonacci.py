'''
Generate the fibonacci sequence
Fibonacci sequence is characterized by the fact that every number after 
the first two is the sum of the two preceding ones. It typically starts with 0 and 1. 
The sequence goes like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 and so forth

Time Complexity: O(2^n) generates two more calls, leading to an exponential growth
                        in the number of calls as n increases.
Space Complexity: O(n) this is because the maximum depth of the recursion is n
'''

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci_sequence = [fibonacci(i) for i in range(10)]

assert fibonacci_sequence[0] == 0,  "Failed on fibonacci_sequence[0]"
assert fibonacci_sequence[1] == 1,  "Failed on fibonacci_sequence[1]"
assert fibonacci_sequence[3] == 2,  "Failed on fibonacci_sequence[3]"

print("All tests passed!")
