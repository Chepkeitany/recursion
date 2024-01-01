'''
Check if a given number is prime or not
'''

def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True

    square_root_value = number ** 0.5
    return check_divisors(number, 2, square_root_value)


'''
Check if a given number has any divisor from 2 to the square root of 2
'''
def check_divisors(number, divisor, square_root_value):
    if divisor > square_root_value:
        return True # no divisor found from 2 to square_root_value
    if number % divisor == 0:
        return False
    return check_divisors(number, divisor + 1, square_root_value)

assert is_prime(10) == False,   "Failed on is_prime(10)"
assert is_prime(3) ==  True,    "Failed on is_prime(3)"
assert is_prime(1) ==  False,   "Failed on is_prime(1)"
assert is_prime(2) ==  True,    "Failed on is_prime(1)"

print("All tests passed")
