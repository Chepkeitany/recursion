'''
Determine if a key is present in a sorted array or not

It uses a binary search helper to find a key in a sorted array
Time Complexity :  O(log(n))  - where n is the size of input array.
                                The search space is halved at each recursive step.
Space Complexity :  O(log(n)) - There are log(n) recursive calls as the search
                                space is halved at each recursive step.
'''


def binary_search(nums, target):
    """ Checks if a target is present in the nums array """
    return binary_search_helper(nums, 0, len(nums) - 1, target)


def binary_search_helper(nums, low, high, target):
    """ Binary search helper to find a target in a sorted array """
    if low > high:
        return False
    mid = low + (high - low) // 2

    if nums[mid] == target:
        return True
    if nums[mid] > target:
        return binary_search_helper(nums, low, mid - 1, target)
    return binary_search_helper(nums, mid + 1, high, target)


assert binary_search(
    [2, 4, 6, 8, 10], 5) is False, "Failed on binary_search([2, 4, 6, 8, 10], 5)"
assert binary_search(
    [2, 4, 6, 8, 10], 4), "Failed on binary_search([2, 4, 6, 8, 10], 4)"
assert binary_search(
    [2, 3, 5, 7], 3), "Failed on binary_search([2, 3, 5, 7], 3)"
assert binary_search(
    [2, 3, 5, 7], 9) is False, "Failed on binary_search([2, 3, 5, 7], 9)"

print("All tests passed!")
