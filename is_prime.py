'''
Check if a given number is prime or not

It uses a helper function to check if the given number has any divisor
from 2 to the square root of the number
Time Complexity :  O(sqrt(n))  - where n is the given number. This function
                  checks the divisibility of the number from 2 up to its square root
Space Complexity : O(sqrt(n))  - the maximum depth of the recursion is determined by
                                 the square root of the number
'''


def is_prime(number):
    """ Check if a given number is prime or not """
    if number < 2:
        return False
    if number == 2:
        return True

    square_root_value = number ** 0.5
    return check_divisors(number, 2, square_root_value)


def check_divisors(number, divisor, square_root_value):
    """ Check if a number has a divisor from 2 to its square root value """
    if divisor > square_root_value:
        return True  # no divisor found from 2 to square_root_value
    if number % divisor == 0:
        return False
    return check_divisors(number, divisor + 1, square_root_value)

if __name__ == '__main__':
    assert is_prime(10) is False, "Failed on is_prime(10)"
    assert is_prime(3), "Failed on is_prime(3)"
    assert is_prime(1) is False, "Failed on is_prime(1)"
    assert is_prime(2), "Failed on is_prime(1)"

    print("All tests passed")
