'''
Given an array, return the array sorted in ascending order
Time Complexity: Average O(n log n)
                 Worst case: O(n ^ 2) where n is the size of the array
                 Average case is when each recursive call divides the array
                 into roughly two equal halves leading to log n recursive calls.
                 In each call, we do O(n) work in the partitioning process
                 Worst case is when the pivot chosen happens to be either the
                 largest or smallest element leading to unbalanced partitions
                 and we end up with n recursive calls
Space Complexity: Average:    O(log n)
                  Worst case: O(n)
                  Average - good pivot is chosen leading log n recursive calls
                  Worst - poor pivot(largest or smallest element) chosen, the
                  depth of recursive call stack can grow up to n.
'''


def quick_sort(arr):
    """ Given an array, return the array sorted in ascending order """
    if len(arr) <= 1:
        return arr

    # Choosing pivot: we'll use the middle element
    # Many ways to choose pivot: first or last element, middle element
    # random element, using median of three e.t.c
    pivot = len(arr) // 2
    pivot_value = arr[pivot]

    smaller = [x for x in arr if x < pivot_value]
    equal = [x for x in arr if x == pivot_value]
    larger = [x for x in arr if x > pivot_value]

    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == '__main__':
    assert quick_sort([8, 6, 7, 5, 4]) == [4, 5, 6, 7,
                                           8], "Failed on quick_sort([8, 6, 7, 5, 4])"
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4,
                                           5], "Failed on quick_sort([5, 4, 3, 2, 1])"
    assert quick_sort([5]) == [5], "Failed on quick_sort([5])"
    assert quick_sort([2, 1, 0, -2, -1]) == [-2, -1, 0, 1,
                                             2], "Failed on quick_sort([2, 1, 0, -2, -1])"

    print("All tests passed!")
