'''
Sum the first n natural numbers
'''
def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)

print(sum_numbers(5))
print(sum_numbers(3))
print(sum_numbers(1))