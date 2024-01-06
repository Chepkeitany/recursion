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
