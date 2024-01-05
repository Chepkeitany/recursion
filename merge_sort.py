'''
Given an array, return the array sorted in ascending order
'''

def merge_sort(arr):
    # empty array or array of size 1 is sorted
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid] # left half of the array - from 0 to mid
    right = arr[mid:] # right half of the array - from mid to len(arr)

    # recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # merge the two sorted halves
    return merge(left, right)

'''
Combine the two sorted arrays into one sorted array
'''
def merge(left, right):
    merged = []
    # pointers to traverse both left and right arrays
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged



