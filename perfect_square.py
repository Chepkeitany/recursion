'''
Check if a given number is a perfect square or not
'''
def is_perfect_square(num):
    # base case
    if num == 0 or num == 1:
      return True
    return is_perfect_square_helper(num, 0, num)

'''
Helper function that uses binary search to determine
if a number is a perfect square or not
'''
def is_perfect_square_helper(num, low, high):
    if low > high:
      return False

    mid = (low + high) // 2
    mid_square = mid * mid
    if mid_square == num:
      return True
    elif mid_square > num:
      return is_perfect_square_helper(num, low, mid - 1)
    else:
      return is_perfect_square_helper(num, mid + 1, high)

assert is_perfect_square(10) == False,   "Failed on is_perfect_square(10)"
assert is_perfect_square(16) ==  True,    "Failed on is_perfect_square(16)"
assert is_perfect_square(1) ==  True,   "Failed on is_perfect_square(1)"
assert is_perfect_square(2) ==  True,   "Failed on is_perfect_square(2)"
assert is_perfect_square(4) ==  True,    "Failed on is_perfect_square(4)"
print("All tests passed!")
