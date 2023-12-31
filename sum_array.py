'''
Compute sum of elements in an array by recursively adding the current element 
to the sum of remaining elements.
'''

def sum_array(items, i=0):
    if i == len(items):
        return 0
    return items[i] + sum_array(items, i + 1)
