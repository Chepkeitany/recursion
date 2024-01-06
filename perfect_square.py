'''
Check if a given number is a perfect square or not

It uses a helper function that uses binary search to determine
if a number is a perfect square or not
Time Complexity :  O(log(n))  - where n is the given number. This is because we perform
                                binary search which divides the input space into half
                                in each call leading to log(n) calls
Space Complexity :  O(log(n))  - there will be log(n) recursive calls made during
                                 the binary search process
'''


def is_perfect_square(num):
    """ Check if a given number is a perfect square or not """
    # base case
    if num <= 1:
        return True
    return is_perfect_square_helper(num, 0, num)


def is_perfect_square_helper(num, low, high):
    """ Use binary search to determine if a number is a perfect square """
    if low > high:
        return False

    mid = (low + high) // 2
    mid_square = mid * mid
    if mid_square == num:
        return True
    if mid_square > num:
        return is_perfect_square_helper(num, low, mid - 1)
    return is_perfect_square_helper(num, mid + 1, high)


assert is_perfect_square(10) is False, "Failed on is_perfect_square(10)"
assert is_perfect_square(16), "Failed on is_perfect_square(16)"
assert is_perfect_square(1), "Failed on is_perfect_square(1)"
assert is_perfect_square(2) is False, "Failed on is_perfect_square(2)"
assert is_perfect_square(4), "Failed on is_perfect_square(4)"

print("All tests passed!")
