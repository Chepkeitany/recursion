'''
Given an array, return the array sorted in ascending order
Time Complexity: O(n log n) - where n is the size of the input array
                              in each level of recursion, the list is divided
                              into half leading to log(n) recursive calls
                              The merge step takes O(n) time because it is
                              merging two n/2 arrays in each recursive call
                              The total time complexity is n * log (n)
Space Complexity: O(n)      - The merge step requires an extra space to store
                              merged elements from the two sorted arrays
                              This space is proportional to the size of input n
                              Also, the recursive call stack takes space which
                              this is log(n), proportional to the recursive depth
'''


def merge_sort(arr):
    """ Sort an array using merge sort algorithm """
    # empty array or array of size 1 is sorted
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]  # left half of the array - from 0 to mid
    right = arr[mid:]  # right half of the array - from mid to len(arr)

    # recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    """ Combine the two sorted arrays into one sorted array """
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

if __name__ == '__main__':
    assert merge_sort([8, 6, 7, 5, 4]) == [4, 5, 6, 7,
                                        8], "Failed on merge_sort([8, 6, 7, 5, 4])"
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4,
                                        5], "Failed on merge_sort([5, 4, 3, 2, 1])"
    assert merge_sort([5]) == [5], "Failed on merge_sort([5])"
    assert merge_sort([2, 1, 0, -2, -1]) == [-2, -1, 0, 1,
                                            2], "Failed on merge_sort([2, 1, 0, -2, -1])"

    print("All tests passed!")
