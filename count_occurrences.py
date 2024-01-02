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

