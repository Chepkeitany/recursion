'''
Given an array, return the array sorted in ascending order
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Choosing pivot: we'll use the middle element
    # Many ways to choose pivot: first or last element, middle element
    # random element, using median element
    pivot = len(arr) // 2
    pivot_value = arr[pivot]

    smaller = [x for x in arr if x < pivot_value]
    equal = [x for x in arr if x == pivot_value]
    larger = [x for x in arr if x > pivot_value]

    return quick_sort(smaller) + equal + quick_sort(larger)

assert quick_sort([8, 6, 7, 5, 4]) == [4, 5, 6, 7, 8], "Failed on quick_sort([8, 6, 7, 5, 4])"
assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Failed on quick_sort([5, 4, 3, 2, 1])"
assert quick_sort([5]) == [5], "Failed on quick_sort([5])"
assert quick_sort([2, 1, 0, -2, -1]) == [-2, -1, 0, 1, 2], "Failed on quick_sort([2, 1, 0, -2, -1])"

print("All tests passed!")