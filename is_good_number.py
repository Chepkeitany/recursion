'''
Check if a given digit string is a good number.
A digit string is good if the digits (0-indexed) at even indices are even 
and the digits at odd indices are prime ((2, 3, 5, or 7).
'''

from is_prime import is_prime

def is_good_number(s):
    """Check if a digit string s is a good number"""
    return check_is_good_number(s, 0)

def check_is_good_number(s, index):
    """Recursive function to check if digit at index follows the rules of a good number"""
    if index == len(s) - 1:
        return True

    # even index
    if index % 2 == 0:
        # digits at even indices should be even
        if int(s[index]) % 2 != 0:
            return False
        return check_is_good_number(s, index + 1)
    # odd index
    # digits at odd indices should be prime
    if not is_prime(int(s[index])):
        return False
    return check_is_good_number(s, index + 1)

if __name__ == '__main__':
    assert is_good_number('02468') is False, "Failed on is_good_number('02468')"
    assert is_good_number('23478'),          "Failed on is_good_number('23478')"
    assert is_good_number('224365'),         "Failed on is_good_number('224365')"

    print("All tests passed!")
