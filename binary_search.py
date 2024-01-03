'''
Determine if a key is present in a sorted array or not
'''

def binary_search(nums, target):
    return binary_search_helper(nums, 0, len(nums) -1, target)
  
def binary_search_helper(nums, low, high, target):
    if low > high:
        return False
    mid = low + (high - low) // 2

    if nums[mid] == target:
        return True
    elif nums[mid] > target:
        return binary_search_helper(nums, low, mid - 1, target)
    else:
        return binary_search_helper(nums, mid + 1, high, target)
