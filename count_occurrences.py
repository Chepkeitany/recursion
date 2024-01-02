'''
Given an array of numbers and a key, count the frequency of the key
'''
def count_occurrences(arr, key):
    return count_occurrences_helper(arr, key)

def count_occurrences_helper(arr, key, index=0):
    if index >= len(arr):
        return 0

    count = 1 if arr[index] == key else 0

    total_count = count + count_occurrences_helper(arr, key, index + 1)

    return total_count

assert count_occurrences([2, 4, 6, 8, 4], 4) == 2, "Failed on count_occurrences([2, 4, 6, 8, 4], 4)"
assert count_occurrences([2, 4, 6, 8, 4], 2) == 1, "Failed on count_occurrences([2, 4, 6, 8, 4], 2)"
assert count_occurrences([2, 2, 2, 2, 4], 2) == 4, "Failed on count_occurrences([2, 2, 2, 2, 4], 2)"

print("All tests passed!")
