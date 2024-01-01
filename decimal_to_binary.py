'''
Convert a decimal number to its binary representation

Time Complexity : O(log n) - where n is the decimal number. 
                             There are n recursive calls because the algorithm
                             divides the decimal number by 2 in each call
                             until the base case is reached
Space Complexity: O(log n). This is because each recursive call adds a frame
                            to the call stack until the base case is reached.                             
'''

def decimal_to_binary(number):
    if number == 0:
        return ""
    return decimal_to_binary(number // 2) + str(decimal % 2)

assert decimal_to_binary(10) == "1010",   "Failed on decimal_to_binary(10)"
assert decimal_to_binary(3) ==  "11",     "Failed on decimal_to_binary(3)"
assert decimal_to_binary(1) ==  "1",      "Failed on decimal_to_binary(1)"
