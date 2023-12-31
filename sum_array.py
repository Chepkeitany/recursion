'''
Compute sum of elements in an array by recursively adding the current element 
to the sum of remaining elements.

Time Complexity : O(n) - where n is the number of elements in the array.
                         we make a single recursive call for each element in the array
                         traversing the entire array once
Space Complexity: O(n) - there will be n recursive calls waiting on the call stack
                         before the base case is reached. Each recursive call
                         adds a new call stack frame
                         consuming additional space leading to a linear stack depth
'''

def sum_array(items, i=0):
    if i == len(items):
        return 0
    return items[i] + sum_array(items, i + 1)

if __name__ == "__main__":
    assert sum_array([2, 4, 6, 1, 3, 5]) == 21, "Test with positive numbers failed"
    assert sum_array([]) == 0, "Test with empty array failed"
    assert sum_array([-1, -2, -3, -4]) == -10, "Test with negative numbers failed"
    assert sum_array([10]) == 10, "Test with single element failed"

    print("All tests passed!")
